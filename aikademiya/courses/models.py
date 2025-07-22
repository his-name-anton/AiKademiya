from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Course(TimeStampedModel):
    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="beginner")
    goal = models.TextField(blank=True)
    language = models.CharField(max_length=10, default="ru")
    is_public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


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
