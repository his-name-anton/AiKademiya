"""Temporal workflows used by the worker."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import timedelta
from typing import Dict, List, Optional

from temporalio import workflow

from .activities import ai_task, save_course_to_db, check_topic, normalize_topic


@dataclass
class CourseState:
    topic: str
    normalized_topic: Optional[str] = None
    category: Optional[str] = None
    outline: Dict[str, any] | None = None
    modules: List[Dict[str, any]] = field(default_factory=list)
    current_module: int = 0
    current_chapter: int = -1
    status: str = "starting"


@workflow.defn
class GenerateCourseWorkflow:
    """Workflow that manages course generation interactively."""

    def __init__(self) -> None:
        self.state = CourseState(topic="")
        self._confirmed: bool = False
        self._next_chapter: bool = False

    @workflow.run
    async def run(self, topic: str) -> int:
        self.state.topic = topic
        self.state.status = "checking"

        await workflow.execute_activity(
            check_topic,
            {"topic": topic},
            schedule_to_close_timeout=timedelta(seconds=60),
        )

        norm = await workflow.execute_activity(
            normalize_topic,
            {"topic": topic},
            schedule_to_close_timeout=timedelta(seconds=60),
        )
        data = json.loads(norm)
        self.state.normalized_topic = data.get("course_title")
        self.state.category = data.get("category_id")

        outline_text = await workflow.execute_activity(
            ai_task,
            "generate_outline",
            {"topic": self.state.normalized_topic},
            schedule_to_close_timeout=timedelta(seconds=60),
        )
        self.state.outline = json.loads(outline_text)
        self.state.status = "waiting_confirmation"

        await workflow.wait_condition(lambda: self._confirmed)
        self.state.status = "generating"
        self._next_chapter = True

        for mod in self.state.outline.get("modules", []):
            module_data = {"title": mod["title"], "chapters": []}
            self.state.modules.append(module_data)
            for chap_title in mod.get("chapters", []):
                await workflow.wait_condition(lambda: self._next_chapter)
                self._next_chapter = False
                self.state.current_module = len(self.state.modules) - 1
                self.state.current_chapter += 1

                content = await workflow.execute_activity(
                    ai_task,
                    "generate_chapter",
                    {"title": chap_title},
                    schedule_to_close_timeout=timedelta(minutes=2),
                )
                quiz_text = await workflow.execute_activity(
                    ai_task,
                    "generate_quiz",
                    {"title": chap_title},
                    schedule_to_close_timeout=timedelta(minutes=2),
                )
                module_data["chapters"].append(
                    {
                        "title": chap_title,
                        "content": content,
                        "quiz": json.loads(quiz_text),
                    }
                )

        course_id = await workflow.execute_activity(
            save_course_to_db,
            {
                "topic": self.state.normalized_topic,
                "title": self.state.outline.get("title"),
                "description": self.state.outline.get("description", ""),
                "modules": self.state.modules,
            },
            schedule_to_close_timeout=timedelta(minutes=5),
        )
        self.state.status = "completed"
        return course_id

    # ------------------------------------------------------------------
    # Signals & queries
    # ------------------------------------------------------------------
    @workflow.signal
    def confirm(self, proceed: bool = True) -> None:
        self._confirmed = proceed

    @workflow.signal
    def next_chapter(self) -> None:
        self._next_chapter = True

    @workflow.query
    def get_state(self) -> dict:
        return {
            "status": self.state.status,
            "topic": self.state.normalized_topic or self.state.topic,
            "category": self.state.category,
            "outline": self.state.outline,
            "current_module": self.state.current_module,
            "current_chapter": self.state.current_chapter,
        }