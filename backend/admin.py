from django.contrib import admin
from backend.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
