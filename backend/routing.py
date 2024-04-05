from django.urls import path
from backend.consumers import NotificationConsumer


websocket_urlpatterns = [
    path(r'ws/socket-server/', NotificationConsumer.as_asgi()),
]
