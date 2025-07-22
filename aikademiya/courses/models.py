from django.conf import settings
from django.db import models
from django.db.models import CharField
from django.utils.text import slugify

from core.models import TimeStampedModel


class Category(TimeStampedModel):
    """Course category."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Course(TimeStampedModel):
    """Model representing a course draft during generation process."""

    STATUS_CHOICES = [
        ('init', 'init'),
        ('topic_verification', 'topic_verification'),
        ('topic_failed_verification', 'topic_failed_verification'),
        ('normalize_and_categorization_topic', 'normalize_and_categorization_topic'),
        ("pending_confirmation", "pending_confirmation"),
        ("confirmed", "confirmed"),
        ("rejected_by_requester", "rejected_by_requester"),
        ("in_progress", "in_progress"),
        ("completed", "completed"),
        ("draft", "draft"),
        ("error", "error"),
    ]

    DIFFICULTY_CHOICES = [
        ("beginner", "beginner"),
        ("intermediate", "intermediate"),
        ("advanced", "advanced"),
    ]

    WRITING_STYLE_CHOICES = [
        ("formal", "formal"),
        ("casual", "casual"),
        ("academic", "academic"),
        ("practical", "practical"),
    ]

    initiated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="initiated_courses",
    )

    original_topic = models.TextField(blank=True)
    normalized_title = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default="beginner")
    writing_style = models.CharField(max_length=20, choices=WRITING_STYLE_CHOICES, default="practical")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="init")
    confirmed_at = models.DateTimeField(null=True, blank=True)

    # legacy fields for future use
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    goal = models.TextField(blank=True)
    language = models.CharField(max_length=10, default="ru")
    is_public = models.BooleanField(default=False)

    def __str__(self) -> CharField:
        return self.normalized_title or self.title


class Module(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=512, blank=True)
    index = models.PositiveIntegerField()

    class Meta:
        unique_together = ("course", "index")
        ordering = ["index"]

    def __str__(self) -> str:
        return self.title


class Chapter(TimeStampedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    content = models.TextField()
    index = models.PositiveIntegerField()
    summary = models.CharField(max_length=512, blank=True)

    class Meta:
        unique_together = ("module", "index")
        ordering = ["index"]

    def __str__(self) -> str:
        return self.title


class CourseValidationLog(TimeStampedModel):
    """Stores requests and responses for course topic validation."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    validation_type = models.CharField(max_length=50)
    request_data = models.JSONField()
    response_data = models.JSONField()
    is_successful = models.BooleanField()
    error_message = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.validation_type} for {self.course_id}"
