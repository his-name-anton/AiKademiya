from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.conf import settings
from core.views import VueAppView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        if user.email:
            send_mail(
                "Welcome to AiKademiya",
                "Thank you for registering!",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
            )

        # Redirect to Vue app profile page
        return redirect("/#/profile")


class ForgotPasswordView(VueAppView):
    """Use Vue app for forgot password page"""
    pass


class ProfileView(LoginRequiredMixin, VueAppView):
    """Use Vue app for profile page"""
    pass


class SettingsView(LoginRequiredMixin, VueAppView):
    """Use Vue app for settings page"""
    pass


