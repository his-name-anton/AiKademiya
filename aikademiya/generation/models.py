from django.conf import settings
from django.db import models
import fernet_fields

from core.models import TimeStampedModel


class GenerationRequest(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prompt = models.TextField()
    response = models.TextField()

    class Meta:
        ordering = ["-created_at"]


class AITaskType(models.Model):
    """Catalog of available AI tasks."""

    code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.title


class AIModel(models.Model):
    """Configuration for external AI models."""

    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    endpoint_url = models.URLField(blank=True)
    api_key = fernet_fields.EncryptedTextField()
    max_tokens = models.PositiveIntegerField(default=1024)
    is_active = models.BooleanField(default=True)

    def masked_api_key(self) -> str:
        if not self.api_key:
            return ""
        return f"{self.api_key[:4]}****{self.api_key[-2:]}"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class PromptTemplate(TimeStampedModel):
    """Prompt templates per task and model."""

    title = models.CharField(max_length=255)
    task_type = models.ForeignKey(AITaskType, on_delete=models.CASCADE)
    template = models.TextField()
    model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.title


class AIRequestLog(models.Model):
    """History of calls to AI models."""

    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, null=True, blank=True)
    task_type = models.ForeignKey(AITaskType, on_delete=models.CASCADE)
    prompt_template = models.ForeignKey(PromptTemplate, on_delete=models.CASCADE)
    model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    request_input = models.JSONField()
    response_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
