from .models import User, Course, Module, Chapter, Question, Enrollment, Subscription, Payment, SubscribeStatus
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('email',)
    list_display = ('email', 'role', 'is_staff', 'is_active', 'subscribe_status')
    list_filter = ('role', 'is_staff', 'is_active', 'subscribe_status')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("role", "subscribe_status")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "role", "subscribe_status", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email",)
    USERNAME_FIELD = "email"


admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(Enrollment)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(SubscribeStatus)
