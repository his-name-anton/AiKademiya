from django.urls import path

from .views import generate_course_view, learn_view, index



urlpatterns = [
    path("", index, name="index"),
    path("generate/", generate_course_view, name="generate"),
    path("learn/", learn_view, name="learn"),
]
