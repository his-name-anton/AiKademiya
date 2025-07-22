from django.urls import path

from . import api_views

app_name = "courses_api"

urlpatterns = [
    path("validate-topic/", api_views.validate_topic, name="validate_topic"),
    path("<int:course_id>/confirm/", api_views.confirm_course, name="confirm_course"),
    path("<int:course_id>/reject/", api_views.reject_course, name="reject_course"),
]
