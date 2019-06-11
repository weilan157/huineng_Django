from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse
from apps.index.models import Tasks, Classify
from easy_comment.models import Comment
from apps.user import models
from apps.index import models
from utils.mixin import LoginRequiredMixin
from .forms import TasksForm
from haystack.views import SearchView
from alipay import AliPay
from django.conf import settings

# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# Create your views here.


class Index(View):
    @staticmethod
    def get(request):
        """显示页面"""
        index_list = Tasks.objects.all()
        return render(request, "index_new.html", {
            "index_list": index_list,
            "index_list1": "",
        })


class IndexForm(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        """显示页面"""
        myform = TasksForm()
        return render(request, "index_form.html", {"myform": myform})

    @staticmethod
    def post(request):
        """进行任务上传处理"""
        tasks_form = TasksForm(request.POST, request.FILES, )
        if tasks_form.is_valid():
            user = request.user.username  # 获取登录的用户名
            # print(user)
            # 获取表单元素
            title = tasks_form.cleaned_data['title']
            describe = tasks_form.cleaned_data['describe']
            if tasks_form.cleaned_data['image'] is None:
                image = "image/1508679309367.jpg"  # 显示默认图片
            else:
                image = tasks_form.cleaned_data['image']  # 很重要，不然无法完成上传，为空
                print(image)
            to_time = request.POST.get('to_time')  # 暂时无法解决
            price = tasks_form.cleaned_data['price']
            # print(title, describe, price, to_time, image)
            # 添加到数据库
            obj = Tasks.objects.create(owner=models.User.objects.get(username=user),
                                       title=title, describe=describe, price=price,
                                       to_time=to_time, image=image)
            # return HttpResponse("上传成功")
            url = reverse('index:AliPay', kwargs={'order_id': obj.id})
            return redirect(url)
            # return redirect(reverse('index:index'), {'errmsg': '上传成功'})
        else:
            return HttpResponse("上传失败")
            # return redirect(reverse('index:index'), {'errmsg': '上传失败'})


class Show(LoginRequiredMixin, View):
    """任务详情"""
    @staticmethod
    def get(request, tasks_id):
        # print(tasks_id)
        tasks = Tasks.objects.get(id=tasks_id)  # 展示任务详情
        # print("--------------------")
        # print(tasks.id)
        user = tasks.owner  # 显示所属用户
        classify_all = Classify.objects.filter(owner__id=tasks.id)  # 获取对应tasks外键的标签表
        # print(user)
        index_list = Tasks.objects.all()  # 展示其他任务
        comment = Comment.objects.filter(object_id=tasks.id)  # 获取对应tasks外键的评论表
        """显示页面"""
        return render(request, "show.html", {"tasks": tasks,
                                             "user": user.username,
                                             "classify": classify_all,
                                             "index_list": index_list,
                                             "comment": comment,
                                             })


class PickOrder(LoginRequiredMixin, View):
    """接单"""
    @staticmethod
    def get(request, tasks_id):
        tasks = Tasks.objects.get(id=tasks_id)
        if str(request.user.username) != str(tasks.owner) and not tasks.picker:
            models.Tasks.objects.filter(id=tasks.id).update(picker=request.user.id, is_receive="待完成")
            return redirect(reverse('user:pick'))
        elif tasks.picker:
            return HttpResponse("来晚了！订单已经被接取")
        elif str(request.user.username) == str(tasks.owner):
            return HttpResponse("不能接自己的订单")
        else:
            return HttpResponse("出现了意外！")
        # return render(request, 'show.html')

    # @staticmethod
    # def post(request):
    #     # return render(request, 'show.html')
    #     return redirect(reverse('index:show'))


class MySearchView(SearchView):
    """搜索返回内容重写,可以实现前后端分离，暂时未完成"""
    def create_response(self):  # 重载create_response来实现接口编写
        context = self.get_context()  # 搜索引擎完成后的内容
        # print(context)
        # keyword = self  .request.GET.get('q', None)  # 关键子为q
        # if not keyword:
        #     return JsonResponse({"status": {"code": 400, "msg": {"error_code": 4450, "error_msg": "关键字错误"}}})
        # content = {"status": {"code": 200, "msg": "ok"}, "data": {
        #     "page": now_page, "next_page": next_page, "sort": '默认排序', }}
        # content_list = []
        # for i in context['page'].object_list:  # 对象列表
        #     set_dict = {
        #         'id': i.object.id, 'name': i.object.name, 'description': i.object.description,
        #         'brand': i.object.commodity.brand, 'describe': i.object.describe,
        #         'integral': i.object.integral, 'mall_price': i.object.mall_price,
        #         'market_price': i.object.market_price, 'inventory': i.object.inventory,
        #         'sales_volume': i.object.sales_volume,
        #     }  # 要返回的字段
        #     if i.object.specificationimage_set.filter(is_show=0):
        #         set_dict['show_image'] = i.object.specificationimage_set.filter(is_show=0)[0].image.url
        #     else:
        #         set_dict['show_image'] = None
        #     content_list.append(set_dict)
        # content["data"].update(dict(goods=content_list))
        # return JsonResponse(content)  # 对对象进行序列化返回json格式数据
        return render(self.request, self.template, context)


# GET /orders/(?P<order_id>\d+)/payment/
class PaymentView(LoginRequiredMixin, View):
    """ 获取支付链接 """
    @staticmethod
    def get(request, order_id):
        # 获取参数：order_id, user
        # user = request.user
        # 查询订单对象，校验订单信息
        # try:
        #     order = OrderInfo.objects.get(
        #         order_id=order_id,
        #         user=user,
        #         status=OrderInfo.ORDER_STATUS_ENUM["UNPAID"],
        #         pay_method=OrderInfo.PAY_METHODS_ENUM["ALIPAY"],
        #     )
        # except OrderInfo.DoesNotExist:
        #     return Response({"message": "订单信息有误"},  status=status.HTTP_400_BAD_REQUEST)
        order = Tasks.objects.get(id=order_id)
        if order:
            # 向支付宝发起请求，获取支付链接参数
            alipay_client = AliPay(
                appid=settings.ALIPAY_APPID,   # 沙箱账号的APPID
                app_notify_url=None,    # 默认回调url，配置 notify_url 需要公网环境
                app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
                alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                sign_type="RSA2",    # RSA 或者 RSA2
                debug=settings.ALIPAY_DEBUG    # 默认False
            )

            # 电脑网站支付，需要跳转到 https://openapi.alipay.com/gateway.do? + order_string
            order_string = alipay_client.api_alipay_trade_page_pay(
                out_trade_no=order_id,  # 订单编号
                total_amount=str(order.price),   # 订单总金额，在数据库中是 Decimal 类型，需要转换
                subject="任务订单",    # 订单标题，可以自己指定
                return_url="http://127.0.0.1:8000/index/index/",  # 支付成功回调url
                notify_url=None     # 可选
            )

            # 拼接支付链接地址
            alipay_url = settings.ALIPAY_URL + "?" + order_string
            return redirect(alipay_url)
        else:
            return HttpResponse("出现了意外！")
