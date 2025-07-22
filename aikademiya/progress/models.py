from django.conf import settings
from django.db import models

from core.models import TimeStampedModel
from courses.models import Course


class Enrollment(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    score = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "course")
