# _*_ coding:utf-8 _*_
# 作者:
# 时间:2019/6/3/10:37
from django.urls import path
from apps.chatroom.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', ChatConsumer),
]
