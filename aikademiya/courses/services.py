from __future__ import annotations

from typing import Any, Dict

import requests
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from .models import Category, Course, CourseValidationLog
import logging
logger = logging.getLogger(__name__)


class N8NService:
    def __init__(self) -> None:
        self.webhook_base_url = settings.N8N_WEBHOOK_URL
        self.timeout = settings.N8N_TIMEOUT
        self.retry_attempts = settings.COURSE_VALIDATION_RETRY_ATTEMPTS

    def _post(self, url: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        last_exc: Exception | None = None
        for _ in range(self.retry_attempts):
            try:
                response = requests.post(url, json=payload, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
        assert last_exc is not None
        raise last_exc

    def check_forbidden_content(self, topic: str) -> Dict[str, Any]:
        webhook_url = f"{self.webhook_base_url}/check-forbidden-content"
        payload = {"topic": topic, "check_type": "course_topic"}
        return self._post(webhook_url, payload)

    def analyze_topic(self, topic: str, categories: list[dict]) -> Dict[str, Any]:
        webhook_url = f"{self.webhook_base_url}/analyze-topic"
        payload = {
            "raw_topic": topic,
            "categories": categories,
        }
        return self._post(webhook_url, payload)



class CourseService:
    def __init__(self) -> None:
        self.n8n = N8NService()

    def _log(
        self,
        course: Course,
        validation_type: str,
        request_data: Dict[str, Any],
        response_data: Dict[str, Any],
        *,
        is_successful: bool,
        error_message: str | None = None,
    ) -> None:
        CourseValidationLog.objects.create(
            course=course,
            validation_type=validation_type,
            request_data=request_data,
            response_data=response_data,
            is_successful=is_successful,
            error_message=error_message or "",
        )

    def _get_or_create_category(self, name: str) -> Category:
        category, _ = Category.objects.get_or_create(name=name, defaults={"slug": name})
        return category

    def _serialize_course(self, course: Course) -> Dict[str, Any]:
        return {
            "course_id": course.id,
            "original_topic": course.original_topic,
            "normalized_title": course.normalized_title,
            "category": {
                "id": course.category.id if course.category else None,
                "name": course.category.name if course.category else None,
                "slug": course.category.slug if course.category else None,
            }
            if course.category
            else None,
            "difficulty": course.difficulty,
            "writing_style": course.writing_style,
            "requires_confirmation": course.status == "pending_confirmation",
        }

    def _check_forbidden_content(self, course: Course, topic: str) -> Dict[str, Any]:
        request_data = {"topic": topic}
        try:
            response = self.n8n.check_forbidden_content(topic)
            self._log(course, "content_check", request_data, response, is_successful=True)
            return response.get("data", {})
        except Exception as exc:  # noqa: BLE001
            self._log(course, "content_check", request_data, {}, is_successful=False, error_message=str(exc))
            raise

    def _analyze_topic(self, course: Course, topic: str) -> Dict[str, Any]:
        existing_categories = list(Category.objects.values("id", "name"))
        categories_payload = [{"id": c["id"], "title": c["name"]} for c in existing_categories]
        request_data = {"raw_topic": topic, "categories": categories_payload}
        course.status = "normalize_and_categorization_topic"
        course.save()
        try:
            response = self.n8n.analyze_topic(topic, categories_payload)
            self._log(course, "analyze_topic", request_data, response, is_successful=True)
            return response
        except Exception as exc:
            self._log(course, "analyze_topic", request_data, {}, is_successful=False, error_message=str(exc))
            raise

    def validate_topic(
            self,
            user_id: int,
            topic: str,
            difficulty: str | None = None,
            writing_style: str | None = None,
    ) -> Dict[str, Any]:
        course = Course.objects.create(
            original_topic=topic,
            initiated_by_id=user_id,
            status="init",
            difficulty=difficulty,
            writing_style=writing_style
        )

        try:
            # Проверка на запрещённый контент
            course.status = "topic_verification"
            course.save()
            content_check_result = self._check_forbidden_content(course, topic)

            if not content_check_result.get("is_allowed", True):
                course.status = "topic_failed_verification"
                course.save()
                return {
                    "status": "error",
                    "error_code": "FORBIDDEN_TOPIC",
                    "message": "Данная тема недоступна для создания курса",
                }

            # Категоризация и нормализация
            course.status = "normalize_and_categorization_topic"
            course.save()

            analyze_result = self._analyze_topic(course, topic)
            data = analyze_result.get("data", {})

            if data.get("category_exists"):
                category = Category.objects.get(id=data["category_id"])
            else:
                category = self._get_or_create_category(data["category_title"])

            course.normalized_title = data["course_title"]
            course.category = category
            course.status = "pending_confirmation"
            course.save()

            return {"status": "success", "data": self._serialize_course(course)}

        except Exception as exc:
            logger.exception("Ошибка при валидации темы курса")
            course.status = "error"
            course.save()
            raise

    def confirm_course(
        self,
        course: Course,
        difficulty: str | None = None,
        writing_style: str | None = None,
    ) -> Course:
        if difficulty:
            course.difficulty = difficulty
        if writing_style:
            course.writing_style = writing_style
        course.status = "confirmed"
        course.confirmed_at = timezone.now()
        course.save()
        return course

    def reject_course(self, course: Course) -> Course:
        course.status = "rejected_by_requester"
        course.save()
        return course
