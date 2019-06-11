# _*_ coding:utf-8 _*_
# 作者:
# 时间:2019/6/3/10:34
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from apps.chatroom.routing import *

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
