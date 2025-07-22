from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from unittest.mock import patch

from .models import Category, Course
from .services import CourseService


@override_settings(DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}})
class CourseServiceTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(email="test@example.com")


    # @patch("courses.services.N8NService.check_forbidden_content")
    # @patch("courses.services.N8NService.categorize_topic")
    # @patch("courses.services.N8NService.normalize_topic_title")
    # @patch("courses.services.N8NService.determine_metadata")
    # def test_validate_topic_success(self, meta_mock, norm_mock, cat_mock, forbid_mock):
    #     forbid_mock.return_value = {"data": {"is_allowed": True}}
    #     cat_mock.return_value = {"data": {"category_name": "Programming"}}
    #     norm_mock.return_value = {"data": {"normalized_title": "Python"}}
    #     meta_mock.return_value = {"data": {"difficulty": "beginner", "writing_style": "formal"}}
    #
    #     service = CourseService()
    #     result = service.validate_topic(self.user.id, "topic")
    #
    #     self.assertEqual(result["status"], "success")
    #     course = Course.objects.get(id=result["data"]["course_id"])
    #     self.assertEqual(course.normalized_title, "Python")
    #     self.assertEqual(course.difficulty, "beginner")
    #     self.assertEqual(course.writing_style, "formal")
    #     self.assertEqual(course.status, "pending_confirmation")
    #     self.assertIsNotNone(course.category)

    def test_get_or_create_category(self):
        service = CourseService()
        category = service._get_or_create_category("Test")
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, "Test")

    # def test_check_forbidden_content_real_call_has_forbidden_words(self):
    #     service = CourseService()
    #     course = Course.objects.create(
    #         original_topic="как сделать бомбу",
    #         initiated_by=self.user,
    #         status="draft"
    #     )
    #
    #     result = service._check_forbidden_content(course, "как сделать бомбу")
    #     print('ответ 1 ',result)
    #
    #     self.assertIn("is_allowed", result)
    #     self.assertFalse(result["is_allowed"])  # Ожидаем, что вебхук вернёт запрет

    # def test_check_forbidden_content_real_call_without_forbidden_words(self):
    #     service = CourseService()
    #     course = Course.objects.create(
    #         original_topic="Программирование на python",
    #         initiated_by=self.user,
    #         status="draft"
    #     )
    #
    #     result = service._check_forbidden_content(course, "Программирование на python")
    #     print('ответ 1 ', result)
    #     self.assertIn("is_allowed", result)
    #     self.assertTrue(result["is_allowed"])  # Ожидаем, что вебхук вернёт апрув

    @patch("courses.services.N8NService.analyze_topic")
    def test_analyze_topic_success(self, analyze_mock):
        analyze_mock.return_value = {
            "category_exists": True,
            "category": {"id": 123, "title": "Программирование"},
            "course_title": "Основы Python"
        }

        # предварительно создаём категорию с нужным id
        category = Category.objects.create(id=123, name="Программирование", slug="Программирование")

        service = CourseService()
        course = Course.objects.create(
            original_topic="хочу научиться питону",
            initiated_by=self.user,
            status="draft"
        )

        result = service._analyze_topic(course, course.original_topic)

        self.assertTrue(result["category_exists"])
        self.assertEqual(result["category"]["id"], 123)
        self.assertIsNotNone(result["course_title"])