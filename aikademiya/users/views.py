from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.conf import settings

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

        return redirect("profile")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
