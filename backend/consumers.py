import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected'}))

    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status': 'notification is received'}))

    def disconnect(self, *args, **kwargs):
        print('disconnected')

    def send_notification(self, event):
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'message': data}))
