from django.contrib import admin
from .models import AITaskType, AIModel, PromptTemplate, AIRequestLog, GenerationRequest


@admin.register(AITaskType)
class AITaskTypeAdmin(admin.ModelAdmin):
    list_display = ("code", "title")


@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ("name", "provider", "is_active", "masked_api_key")
    readonly_fields = ("masked_api_key",)

    def get_fields(self, request, obj=None):
        fields = ["name", "provider", "endpoint_url", "max_tokens", "is_active", "masked_api_key"]
        if request.user.is_superuser:
            fields.insert(3, "api_key")
        return fields


@admin.register(PromptTemplate)
class PromptTemplateAdmin(admin.ModelAdmin):
    list_display = ("title", "task_type", "model", "is_active", "created_by")
    list_filter = ("task_type", "model", "is_active")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(AIRequestLog)
class AIRequestLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "task_type", "model", "course")
    readonly_fields = ("created_at", "request_input", "response_output")


@admin.register(GenerationRequest)
class GenerationRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
