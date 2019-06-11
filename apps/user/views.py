from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from apps.user import models
from apps.user.models import User
from apps.index.models import Tasks
from utils.mixin import LoginRequiredMixin
from .forms import UserinfoForm
from datetime import timedelta
from django.core import signing  # 解密加密模块
from django.core.signing import (BadSignature, SignatureExpired)  # 验证错误模块
import re

#
# # 注册/user/register
# class RegisterView(View):
#     """注册"""
#     @staticmethod  # 将被装饰的函数从类中分离出来，该函数不能访问类的属性，简单说可以将该函数理解为一个独立的函数，不允许使用self。
#     def get(request):
#         """显示注册页面"""
#         return render(request, 'register.html')
#
#     @staticmethod
#     def post(request):
#         """进行注册处理"""
#         # 接收数据
#         username = request.POST.get('user_name')
#         password = request.POST.get('pwd')
#         email = request.POST.get('email')
#         allow = request.POST.get('allow')
#
#         # 进行数据校验
#         if not all([username, password, email]):
#             # 数据不完整
#             return render(request, 'register.html', {'errmsg': '数据不完整'})
#
#         # 校验邮箱
#         if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
#             return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
#
#         if allow != 'on':
#             return render(request, 'register.html', {'errmsg': '请同意协议'})
#
#         # 校验用户名是否重复
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             # 用户名不存在
#             user = None
#
#         if user:
#             # 用户名已存在
#             return render(request, 'register.html', {'errmsg': '用户名已存在'})
#
#         # 进行业务处理: 进行用户注册
#         user = User.objects.create_user(username, email, password)
#         user.is_active = 0
#         user.save()
#         # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密
#         # 加密用户的身份信息，生成激活token
#         token = signing.dumps(user.id)
#         email = [email]
#         # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/+信息
#         msg_url = 'http://127.0.0.1:8000/user/active/'+token
#         print(msg_url)
#         msg = '<a href=%s>点击激活</a>' % msg_url
#         send_mail(username, '', settings.EMAIL_FROM, email, html_message=msg)
#         # send_mail('标题', '内容', settings.EMAIL_FROM, '目标邮箱')
#         # 返回应答, 跳转到首页
#         return redirect(reverse('index:index'))
#
#
# # 激活
# class ActiveView(View):
#     """用户激活"""
#     @staticmethod
#     def get(request, token):
#         """进行用户激活"""
#         # 进行解密，获取要激活的用户信息
#         try:
#             # 解密，设置1小时过期
#             user_id = signing.loads(token, max_age=timedelta(seconds=3600))
#             # 根据id获取用户信息
#             user = User.objects.get(id=user_id)
#             user.is_active = 1
#             user.save()
#             # 跳转到登录页面
#             return redirect(reverse('user:login'))
#         except SignatureExpired:
#             # 激活链接已过期
#             return HttpResponse('激活链接已过期')
#         except BadSignature:
#             return HttpResponse('无效的激活码')
#
#
# # 登录/user/login
# class LoginView(View):
#     """登录"""
#     @staticmethod
#     def get(request):
#         """显示登录页面"""
#         # 判断是否记住了用户名
#         if 'username' in request.COOKIES:
#             username = request.COOKIES.get('username')
#             checked = 'checked'
#         else:
#             username = ''
#             checked = ''
#         # 使用模板
#         return render(request, 'login.html', {'username': username, 'checked': checked})
#
#     @staticmethod
#     def post(request):
#         """登录校验"""
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             # 接收数据
#             username = request.POST.get('username')
#             password = request.POST.get('pwd')
#
#             # # 校验数据
#             # if not all([username, password]):
#             #     return render(request, 'login.html', {'errmsg': '数据不完整'})
#
#             # 业务处理:登录校验
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 # 用户名密码正确
#                 if user.is_active:
#                     # 用户已激活
#                     # 记录用户的登录状态
#                     login(request, user)
#                     # 获取登录后跳转的地址
#                     next_url = request.GET.get('next', reverse('index:index'))
#                     # 跳转到首页
#                     response = redirect(next_url)  # HttpResponseRedirect
#                     # 判断是否需要记住用户名
#                     remember = request.POST.get('remember')
#                     if remember == 'on':
#                         # 记住用户名
#                         response.set_cookie('username', username, max_age=7*24*3600)
#                     else:
#                         response.delete_cookie('username')
#                     # 返回response
#                     return response
#                 else:
#                     # 用户未激活
#                     return render(request, 'login.html', {'errmsg': '账户未激活'})
#             else:
#                 # 用户名或密码错误
#                 return render(request, 'login.html', {'errmsg': '用户名或密码错误'})
#         else:
#             return render(request, 'login.html')
#
#
# class LogoutView(View):
#     """退出登录"""
#     @staticmethod
#     def get(request):
#         logout(request)
#         return render(request, 'chat.html')


class UserInfoView(LoginRequiredMixin, View):
    """用户中心"""
    @staticmethod
    def get(request):
        return render(request, 'user_center_info.html')

    @staticmethod
    def post(request):
        # 更改个人资料
        info_form = UserinfoForm(request.POST, request.FILES, )
        if info_form.is_valid():
            user = request.user.username  # 获取登录的用户名
            avatar = info_form.cleaned_data['avatar']  # 很重要，不然无法完成上传，为空
            # 改头像
            mod = models.User.objects.get(username=user)  # 打开相应数据库
            mod.avatar = avatar  # 改头像
            mod.save()  # 保存
            return render(request, 'user_center_info.html')
        else:
            return render(request, 'user_center_info.html')


class UserOrderView(LoginRequiredMixin, View):
    """发布订单"""
    @staticmethod
    def get(request):
        user = request.user.username  # 获取登录的用户名
        user = User.objects.get(username=user)
        tasks_all = Tasks.objects.filter(owner__id=user.id).order_by('-create_time')
        return render(request, 'user_center_order.html', {"tasks": tasks_all})


class PickOrderView(LoginRequiredMixin, View):
    """领取订单"""
    @staticmethod
    def get(request):
        user = request.user.username  # 获取登录的用户名
        user = User.objects.get(username=user)
        tasks_all = Tasks.objects.filter(picker__id=user.id).order_by('-create_time')
        return render(request, 'user_center_pick.html', {"tasks": tasks_all})
