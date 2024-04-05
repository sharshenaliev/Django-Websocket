from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from backend.models import Notification


@receiver(post_save, sender=User)
def choice_handler(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(text=f'User {instance.username} was created')
