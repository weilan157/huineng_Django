from django.conf.urls import url
from django.urls import path
# from apps.index import views
from apps.index.views import Index, Show, PickOrder, IndexForm, PaymentView


app_name = 'index'
urlpatterns = [
    path('AliPay/<order_id>/', PaymentView.as_view(), name='AliPay'),  # 支付链接
    url(r'^index_form/', IndexForm.as_view(), name='index_form'),
    url(r'^pick_order/(?P<tasks_id>\d+)/$', PickOrder.as_view(), name='pick_order'),  # 接单
    url(r'^show/(?P<tasks_id>\d+)/$', Show.as_view(), name='show'),  # 详情 接受任务id
    url(r'index/', Index.as_view(), name='index'),  # 首页
    ]
