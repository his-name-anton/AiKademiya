from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView

def index(request):
    return render(request, "index.html")


def generate_course_view(request):
    allowed = request.user.is_authenticated
    return render(request, "generate.html", {"allowed": allowed, "debug": settings.DEBUG})


def learn_view(request):
    allowed = request.user.is_authenticated
    return render(request, "learn.html", {"allowed": allowed})


# core/views.py


class VueAppView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['debug'] = settings.DEBUG
        return context