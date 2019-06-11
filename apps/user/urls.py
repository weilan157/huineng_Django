from django.conf.urls import url
# from django.urls import path, include, re_path
from apps.user.views import *
# from user.views import *
app_name = 'user'
urlpatterns = (
    # url(r'^register$', views.register, name='register'), # 注册
    # url(r'^register_handle$', views.register_handle, name='register_handle'), # 注册处理
    # url(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    # url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    # url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    # url(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销
    url(r'^info$', UserInfoView.as_view(), name='info'),  # 用户中心
    url(r'^order$', UserOrderView.as_view(), name='order'),  # 订单
    url(r'^pick$', PickOrderView.as_view(), name='pick'),  # 接单
)
