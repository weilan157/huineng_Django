"""huineng1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.index.views import MySearchView
from django.contrib import admin
from django.urls import include
import xadmin
from django.conf.urls import url
from apps.user import urls as app_url
from apps.index import urls as index_url
from apps.chatroom import urls as chatroom_url
# from django.views.generic import TemplateView

from huineng1 import settings
from huineng1.settings import MEDIA_ROOT
from django.views.static import serve
from django.conf.urls.static import static
from apps.index.views import Index
import notifications.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 自带后台，有站点
    url(r'^xadmin/', xadmin.site.urls),  # 第三方后台
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 富文本编辑器
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 配置上传文件的访问处理
    url(r'^easy_comment/', include('easy_comment.urls')),  # 评论
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),  # 通知
    # url(r'^not found/', include(index_url, namespace='not found')),  # 404
    url(r'^accounts/', include('allauth.urls')),  # 第三方登录，注册
    url(r'^user/', include(app_url, namespace='user')),  # 用户模块
    url(r'^search/', MySearchView(), name='haystack_search'),  # 全局搜索
    url(r'^index/', include(index_url, namespace='index')),  # 首页模块
    url(r'^chatroom/', include(chatroom_url, namespace='chatroom')),  # 聊天模块
    url(r'', Index.as_view()),  # 首页
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
