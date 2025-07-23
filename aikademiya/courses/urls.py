from django.urls import path

from .views import generate_course, course_status, confirm_course, next_chapter

app_name = "courses"

urlpatterns = [
    path("api/generate/", generate_course, name="generate"),
    path("api/status/<str:workflow_id>/", course_status, name="status"),
    path("api/confirm/<str:workflow_id>/", confirm_course, name="confirm"),
    path("api/next/<str:workflow_id>/", next_chapter, name="next"),
]
