from django.contrib import admin

from .models import SubscribeStatus, Subscription, Payment

admin.site.register(SubscribeStatus)
admin.site.register(Subscription)
admin.site.register(Payment)
