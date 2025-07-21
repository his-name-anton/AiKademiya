from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from django.conf import settings

from .forms import CustomUserCreationForm


def index(request):
    return render(request, "index.html")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        if user.email:
            send_mail(
                "Welcome to AiKademiya",
                "Thank you for registering!",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
            )
        return response


class ProfileView(TemplateView):
    template_name = "profile.html"

    @login_required
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def generate_course_view(request):
    allowed = request.user.is_authenticated
    return render(request, "generate.html", {"allowed": allowed})


def learn_view(request):
    allowed = request.user.is_authenticated
    return render(request, "learn.html", {"allowed": allowed})
