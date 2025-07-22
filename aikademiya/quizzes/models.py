from django.db import models

from core.models import TimeStampedModel
from courses.models import Chapter


class Question(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    options = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.text
