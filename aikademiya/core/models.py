from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class SubscribeStatus(models.Model):
    STATUS_CHOICES = [
        ("new", "new"),
        ("active", "active"),
        ("disabled", "disabled"),
        ("expire", "expire"),
    ]

    name = models.CharField(max_length=20, choices=STATUS_CHOICES, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None  # Удаляем username
    email = models.EmailField(unique=True)

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    subscribe_status = models.ForeignKey(
        'SubscribeStatus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Course(TimeStampedModel):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    goal = models.TextField(blank=True)
    language = models.CharField(max_length=10, default='ru')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Module(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=512, blank=True)
    index = models.PositiveIntegerField()

    class Meta:
        unique_together = ('course', 'index')
        ordering = ['index']

    def __str__(self):
        return self.title

class Chapter(TimeStampedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)
    content = models.TextField()
    index = models.PositiveIntegerField()
    summary = models.CharField(max_length=512, blank=True)

    class Meta:
        unique_together = ('module', 'index')
        ordering = ['index']

    def __str__(self):
        return self.title

class Question(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    options = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Enrollment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    score = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'course')

class Subscription(TimeStampedModel):
    PLAN_CHOICES = [
        ('Free', 'Free'),
        ('Pro', 'Pro'),
        ('Enterprise', 'Enterprise'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)

class Payment(TimeStampedModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled'),
    ]
    TYPE_CHOICES = [
        ('subscription', 'Subscription'),
        ('one-time', 'One-time'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default='RUB')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

