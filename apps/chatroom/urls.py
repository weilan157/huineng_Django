# _*_ coding:utf-8 _*_
# 作者:
# 时间:2019/5/30/20:08
from django.conf.urls import url
from django.urls import path
from apps.chatroom import views as v


app_name = 'chatroom'
urlpatterns = [
    # url(r'chat/', ChatView.as_view(), name='chat'),  # 首页
    path('index/', v.index),
    ]
