from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Course, Module, Chapter, Question, Enrollment, Subscription, Payment

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {"fields": ("role",)}),
    )

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(Enrollment)
admin.site.register(Subscription)
admin.site.register(Payment)
