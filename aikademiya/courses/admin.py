from django.contrib import admin

from .models import Course, Module, Chapter, Category

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Chapter)
admin.site.register(Category)
