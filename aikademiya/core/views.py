from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from django.conf import settings

from .forms import CustomUserCreationForm


def index(request):
    return render(request, "index.html")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # 🔹 Войти сразу после регистрации

        if user.email:
            send_mail(
                "Welcome to AiKademiya",
                "Thank you for registering!",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
            )

        return redirect("profile")  # 🔹 Редирект в профиль


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


def generate_course_view(request):
    allowed = request.user.is_authenticated
    return render(request, "generate.html", {"allowed": allowed})


def learn_view(request):
    allowed = request.user.is_authenticated
    return render(request, "learn.html", {"allowed": allowed})
