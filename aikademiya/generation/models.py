from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class GenerationRequest(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prompt = models.TextField()
    response = models.TextField()

    class Meta:
        ordering = ["-created_at"]
