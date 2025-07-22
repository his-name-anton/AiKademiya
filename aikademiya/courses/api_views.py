from __future__ import annotations

import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Course
from .services import CourseService


@csrf_exempt
@login_required
@require_POST
def validate_topic(request):
    try:
        payload = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "error_code": "VALIDATION_ERROR", "message": "Invalid JSON"}, status=400)

    topic = payload.get("topic")
    if not topic:
        return JsonResponse({"status": "error", "error_code": "VALIDATION_ERROR", "message": "Topic is required"}, status=400)

    service = CourseService()
    try:
        result = service.validate_topic(request.user.id, topic)
        return JsonResponse(result)
    except requests.exceptions.Timeout:
        return JsonResponse({"status": "error", "error_code": "N8N_TIMEOUT", "message": "n8n timeout"}, status=502)
    except requests.exceptions.RequestException:
        return JsonResponse({"status": "error", "error_code": "N8N_ERROR", "message": "n8n error"}, status=502)


@csrf_exempt
@login_required
@require_POST
def confirm_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id, initiated_by=request.user)
    payload = json.loads(request.body or "{}")
    if not payload.get("confirmed", False):
        return JsonResponse({"status": "error", "error_code": "VALIDATION_ERROR", "message": "Confirmation required"}, status=400)

    service = CourseService()
    service.confirm_course(course, difficulty=payload.get("difficulty"), writing_style=payload.get("writing_style"))
    return JsonResponse({"status": "success", "data": service._serialize_course(course)})


@csrf_exempt
@login_required
@require_POST
def reject_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id, initiated_by=request.user)
    service = CourseService()
    service.reject_course(course)
    return JsonResponse({"status": "success"})
