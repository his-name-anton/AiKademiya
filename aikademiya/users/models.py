from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from core.models import TimeStampedModel
from billing.models import SubscribeStatus


class UserManager(BaseUserManager):
    """Custom manager for User model with email as unique identifier."""

    use_in_migrations = True

    def _create_user(self, email: str, password: str | None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        if "subscribe_status" not in extra_fields or extra_fields["subscribe_status"] is None:
            try:
                extra_fields["subscribe_status"] = SubscribeStatus.objects.get(name="new")
            except SubscribeStatus.DoesNotExist:
                extra_fields["subscribe_status"] = None

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str | None = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str | None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)
    OCCUPATION_CHOICES = [
        ('school', 'Учусь в школе'),
        ('student', 'Студент'),
        ('employed', 'Работаю'),
        ('freelancer', 'Фриланс'),
        ('unemployed', 'Не работаю'),
        ('other', 'Другое'),
    ]

    occupation = models.CharField(
        max_length=50,
        choices=OCCUPATION_CHOICES,
        null=True,
        blank=True
    )
    SEX_CHOICES = [
        ("male", "Мужской"),
        ("female", "Женский"),
    ]
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, blank=True)

    ROLE_CHOICES = [
        ("student", "Student"),
        ("admin", "Admin"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    subscribe_status = models.ForeignKey(
        SubscribeStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
