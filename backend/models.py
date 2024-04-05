from django.db import models
from django.contrib.auth.models import User
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    seller = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Продавец')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.name)


class Notification(models.Model):
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return self.text

    def save(self, *args, **kwars):
        channel_layer = get_channel_layer()
        objs = User.objects.all().count()
        data = {'total users': objs, 'message': self.text}
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwars)
