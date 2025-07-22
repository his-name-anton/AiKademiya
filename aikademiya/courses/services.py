from __future__ import annotations

from typing import Any, Dict

import requests
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from .models import Category, Course, CourseValidationLog


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

    def categorize_topic(self, topic: str) -> Dict[str, Any]:
        webhook_url = f"{self.webhook_base_url}/categorize-topic"
        payload = {
            "topic": topic,
            "existing_categories": list(Category.objects.values_list("name", flat=True)),
        }
        return self._post(webhook_url, payload)

    def normalize_topic_title(self, topic: str) -> Dict[str, Any]:
        webhook_url = f"{self.webhook_base_url}/normalize-title"
        payload = {"original_topic": topic, "target_type": "course_title"}
        return self._post(webhook_url, payload)

    def determine_metadata(self, topic: str) -> Dict[str, Any]:
        webhook_url = f"{self.webhook_base_url}/determine-metadata"
        payload = {"topic": topic}
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

    def _categorize_topic(self, course: Course, topic: str) -> Dict[str, Any]:
        request_data = {"topic": topic}
        try:
            response = self.n8n.categorize_topic(topic)
            self._log(course, "categorization", request_data, response, is_successful=True)
            return response.get("data", {})
        except Exception as exc:  # noqa: BLE001
            self._log(course, "categorization", request_data, {}, is_successful=False, error_message=str(exc))
            raise

    def _normalize_topic_title(self, course: Course, topic: str) -> Dict[str, Any]:
        request_data = {"topic": topic}
        try:
            response = self.n8n.normalize_topic_title(topic)
            self._log(course, "normalization", request_data, response, is_successful=True)
            return response.get("data", {})
        except Exception as exc:  # noqa: BLE001
            self._log(course, "normalization", request_data, {}, is_successful=False, error_message=str(exc))
            raise

    def _determine_course_metadata(self, course: Course, topic: str) -> Dict[str, Any]:
        request_data = {"topic": topic}
        try:
            response = self.n8n.determine_metadata(topic)
            self._log(course, "determine_metadata", request_data, response, is_successful=True)
            return response.get("data", {})
        except Exception as exc:  # noqa: BLE001
            self._log(course, "determine_metadata", request_data, {}, is_successful=False, error_message=str(exc))
            return {}

    def validate_topic(self, user_id: int, topic: str) -> Dict[str, Any]:
        with transaction.atomic():
            course = Course.objects.create(original_topic=topic, initiated_by_id=user_id, status="draft")
            try:
                content_check_result = self._check_forbidden_content(course, topic)
                if not content_check_result.get("is_allowed", True):
                    course.status = "rejected"
                    course.save()
                    return {
                        "status": "error",
                        "error_code": "FORBIDDEN_TOPIC",
                        "message": "Данная тема недоступна для создания курса",
                    }
                categorization_result = self._categorize_topic(course, topic)
                category = self._get_or_create_category(categorization_result.get("category_name", "Other"))
                normalization_result = self._normalize_topic_title(course, topic)
                metadata_result = self._determine_course_metadata(course, topic)

                course.normalized_title = normalization_result.get("normalized_title", "")
                course.category = category
                course.difficulty = metadata_result.get("difficulty", "beginner")
                course.writing_style = metadata_result.get("writing_style", "practical")
                course.status = "pending_confirmation"
                course.save()

                return {"status": "success", "data": self._serialize_course(course)}
            except Exception:
                course.status = "rejected"
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
        course.status = "rejected"
        course.save()
        return course
