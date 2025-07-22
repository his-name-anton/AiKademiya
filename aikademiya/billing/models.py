from django.db import models
from django.conf import settings

from core.models import TimeStampedModel


class SubscribeStatus(models.Model):
    STATUS_CHOICES = [
        ("new", "new"),
        ("active", "active"),
        ("disabled", "disabled"),
        ("expire", "expire"),
    ]

    name = models.CharField(max_length=20, choices=STATUS_CHOICES, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "subscribe_status"

    def __str__(self) -> str:
        return self.name


class Subscription(TimeStampedModel):
    PLAN_CHOICES = [
        ("Free", "Free"),
        ("Pro", "Pro"),
        ("Enterprise", "Enterprise"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)


class Payment(TimeStampedModel):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("canceled", "Canceled"),
    ]
    TYPE_CHOICES = [
        ("subscription", "Subscription"),
        ("one-time", "One-time"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default="RUB")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    payment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
