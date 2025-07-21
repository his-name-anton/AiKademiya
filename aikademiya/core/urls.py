from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, ProfileView, generate_course_view, learn_view, index

urlpatterns = [
    path("", index, name="index"),
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("generate/", generate_course_view, name="generate"),
    path("learn/", learn_view, name="learn"),
]
