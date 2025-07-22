from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def generate_course_view(request):
    allowed = request.user.is_authenticated
    return render(request, "generate.html", {"allowed": allowed})


def learn_view(request):
    allowed = request.user.is_authenticated
    return render(request, "learn.html", {"allowed": allowed})
