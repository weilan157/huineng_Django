# _*_ coding:utf-8 _*_
# 作者:
# 时间:2019/6/3/10:39
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from apps.user import models


class ChatConsumer(WebsocketConsumer):
    """当WebSocket连接打开时调用"""
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.scope['url_route']['kwargs']['room_name'])
        self.room_group_name = 'chat_%s' % self.room_name
        # 加入聊天室组
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(async_to_sync)
        print(self.room_group_name)
        print(self.channel_name)
        print("0.1")
        print(self.channel_layer.group_add)
        print("1")
        self.accept()

    def disconnect(self, close_code):
        """当WebSocket连接关闭时调用"""
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        """收到消息后调用"""
        text_data_json = json.loads(text_data)
        print(text_data_json)
        print("1.1")
        message = text_data_json['text']
        print(message)
        print(text_data_json['user'])
        print("2")

        # 向房间组发送消息
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",  # 指定了消息处理的函数
                "text": text_data_json['text'],
                "user": text_data_json['user'],
            }
        )

    # 接收来自房间组的消息
    def chat_message(self, event):
        """消息处理的函数"""
        user = models.User.objects.get(username=event['user'])
        # 向WebSocket发送消息
        self.send(text_data=json.dumps({
            "text": event['text'],
            "user": event['user'],
            "avatar": str(user.avatar),
        }))
