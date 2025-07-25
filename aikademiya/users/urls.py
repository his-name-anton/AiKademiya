from django.contrib.auth import views as auth_views
from django.urls import path

from .views import SignUpView, ProfileView, SettingsView, ForgotPasswordView

urlpatterns = [
    # path("register/", SignUpView.as_view(), name="register"),
    # path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    # path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    # path("profile/", ProfileView.as_view(), name="profile"),
    # path("settings/", SettingsView.as_view(), name="settings"),
]
