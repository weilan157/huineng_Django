from django.db import models
from db.base_model import BaseModel
from apps.user.models import User
# Create your models here.


class ChatLog(BaseModel):
    """聊天记录"""
    # create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    chat_describe = models.CharField(verbose_name='聊天内容', max_length=255)
    chat_user = models.ForeignKey(User, verbose_name='发送用户',  related_name='chat_user',
                                  on_delete=models.CASCADE, null=True)
    to_chat_user = models.ForeignKey(User, verbose_name='接收用户',  related_name='to_chat_user',
                                     on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '聊天记录'
        verbose_name_plural = verbose_name


class ChatGroup(models.Model):
    """聊天分组"""
    group = models.CharField(verbose_name='分组名', max_length=10, default="未命名分组")
    chat_owned = models.ForeignKey(User, verbose_name='所属用户',  related_name='chat_owned',
                                   on_delete=models.CASCADE, null=True)
    chat_log = models.ForeignKey(ChatLog, verbose_name='组内成员',  related_name='chat_log',
                                 on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '聊天分组'
        verbose_name_plural = verbose_name
