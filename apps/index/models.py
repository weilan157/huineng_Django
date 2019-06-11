from django.db import models
from db.base_model import BaseModel
from apps.user.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
import os

# Create your models here.


def upload_directory_path(tasks, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    path = os.path.join("user", str(tasks.owner), "tasks", filename)
    return path


class Tasks(BaseModel):
    """任务模型类"""
    owner = models.ForeignKey(User, verbose_name='发布用户',  related_name='owner', on_delete=models.CASCADE, null=True)
    picker = models.ForeignKey(User, verbose_name='接单用户', related_name='picker', on_delete=models.CASCADE, null=True,
                               blank=True)
    title = models.CharField(verbose_name='任务标题', max_length=20)
    describe = RichTextUploadingField(config_name='my_config', verbose_name='任务内容')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')
    price = models.DecimalField(max_digits=10, verbose_name='任务酬金', decimal_places=2)
    to_time = models.DateTimeField(verbose_name='截至时间')
    num = models.IntegerField(default=0, verbose_name='访问量')
    num_max = models.IntegerField(default=10, verbose_name='发布上限')
    receive_name = models.IntegerField(default=0, verbose_name='领取人')
    image = models.ImageField(verbose_name='任务描述图片', upload_to=upload_directory_path,
                              default=u"image/1508679309367.jpg")
    is_receive = models.CharField(verbose_name='任务状态', max_length=6,
                                  choices=(('待接取', '待接取'),
                                           ('待完成', '待完成'),
                                           ('已完成', '已完成')),
                                  default='待接取')

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Examine(BaseModel):
    """审核模型类"""
    user = models.ForeignKey(Tasks, verbose_name='所属任务', on_delete=models.CASCADE)
    is_examine = models.CharField(max_length=6, choices=(('待审核', '未审核'), ('已审核', '已审核'), ('未通过', '未通过')),
                                  default='待审核', verbose_name='审核状态')
    num_examine = models.IntegerField(default=0, verbose_name='审核次数')

    class Meta:
        verbose_name = '审核'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class Classify(models.Model):
    """分类模型类"""
    owner = models.ForeignKey(Tasks, verbose_name='所属任务', on_delete=models.CASCADE)
    label = models.CharField(max_length=6, verbose_name='标签')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.owner
