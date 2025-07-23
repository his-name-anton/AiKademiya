"""Activity functions for Temporal workers."""

from __future__ import annotations

import json
import os
from typing import Any, Dict

from temporalio import activity


def _setup_django() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aikademiya.settings")
    import django  # noqa: WPS433

    django.setup()


@activity.defn
async def ai_task(task_code: str, params: Dict[str, Any]) -> str:
    """Execute an AI task using configuration from the database."""

    _setup_django()
    from aikademiya.generation.models import AITaskType, PromptTemplate, AIRequestLog
    from aikademiya.generation.openai_utils import call_openai, render_template

    task = AITaskType.objects.get(code=task_code)
    template = (
        PromptTemplate.objects.select_related("model")
        .filter(task_type=task, is_active=True)
        .order_by("-id")
        .first()
    )
    if not template:
        raise RuntimeError(f"No active template for task {task_code}")

    prompt = render_template(template.template, params)
    response = await call_openai(template.model, prompt)

    AIRequestLog.objects.create(
        task_type=task,
        prompt_template=template,
        model=template.model,
        request_input=params,
        response_output=response,
    )
    return response


@activity.defn
async def save_course_to_db(course_data: dict) -> int:
    """Persist generated course structure to the database."""

    _setup_django()
    from courses.models import Course, Module, Chapter
    from quizzes.models import Question

    course = Course.objects.create(
        created_by_id=1,
        title=course_data.get("title", course_data.get("topic", "Course")),
        description=course_data.get("description", ""),
    )

    for mod_index, mod in enumerate(course_data.get("modules", []), start=1):
        m = Module.objects.create(course=course, title=mod["title"], index=mod_index)
        for ch_index, ch in enumerate(mod.get("chapters", []), start=1):
            c = Chapter.objects.create(
                module=m,
                title=ch["title"],
                content=ch.get("content", ""),
                index=ch_index,
            )
            for q in ch.get("quiz", {}).get("questions", []):
                Question.objects.create(chapter=c, text=q, options="", correct_answer="")

    return course.id


@activity.defn
async def check_topic(params: dict) -> str:
    """Нормализация темы и категоризация через ИИ"""
    from aikademiya.courses.models import CourseCategory
    task_code = "check_topic"

    return await ai_task(task_code, params)


@activity.defn
async def normalize_topic(params: dict) -> str:
    """Нормализация темы и категоризация через ИИ"""
    from aikademiya.courses.models import CourseCategory
    task_code = "normalize_topic"

    categories = [{"id": c.id, "title": c.name} for c in CourseCategory.objects.all().order_by("id")]
    params["categories"] = categories

    raw_response = await ai_task(task_code, params)

    data = json.loads(raw_response)
    if not data.get("category_exists") and data.get("category_title"):
        new_category, created = CourseCategory.objects.get_or_create(name=data["category_title"])
        data["category_id"] = new_category.id

    return json.dumps(data, ensure_ascii=False)
