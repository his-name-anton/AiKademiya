from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "index.html")


def generate_course_view(request):
    allowed = request.user.is_authenticated
    return render(request, "generate.html", {"allowed": allowed, "debug": settings.DEBUG})


class LearnView(LoginRequiredMixin, TemplateView):
    """Use Vue app for learn page"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debug'] = settings.DEBUG
        return context


def learn_view(request):
    # Redirect to Vue app learn page
    return render(request, "index.html", {"debug": settings.DEBUG})


class VueAppView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debug'] = settings.DEBUG
        return context