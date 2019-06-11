from django.db import models
# from imagekit.models import ProcessedImageField, ImageSpecField
# from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser

from db.base_model import BaseModel
import uuid
import os

# Create your models here.


def user_directory_path(username, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    path = os.path.join("user", str(username), "avatar", filename)
    return path


class User(AbstractUser, BaseModel):
    """用户模型类"""
    # def save(self, *args, **kwargs):
    #     # 当用户更改头像的时候，avatar.name = '文件名'
    #     # 其他情况下avatar.name = 'upload_to/文件名'
    #     if len(self.avatar.name.split('/')) == 1:
    #         # print('before:%s' % self.avatar.name)
    #         # 用户上传图片时，将avatar.name改为 用户名/文件名
    #         self.avatar.name = self.username + '/' + self.avatar.name
    #     super(User, self).save()
    #     # 调用父类的save()方法后，avatar.name就变成了'upload_to/用户名/文件名'
    #     print('after:%s' % self.avatar.name)
    #     print('avatar_path: %s' % self.avatar.path)
    avatar = models.ImageField(upload_to=user_directory_path, verbose_name='头像', default='avatar_default.png')
    # avatar_thumbnail = ImageSpecField(source='avatar',
    #                                   format='JPEG',
    #                                   # 图片将处理成85x85的尺寸
    #                                   processors=[ResizeToFill(85, 85)],
    #                                   options={'quality': 60})
    is_vip = models.BooleanField(default=False, verbose_name='是否会员')
    is_student = models.BooleanField(default=False, verbose_name='是否学生')
    is_enterprise = models.BooleanField(default=False, verbose_name='是否企业')
    is_examine = models.BooleanField(default=False, verbose_name='审核权限')
    is_advertisement = models.BooleanField(default=False, verbose_name='广告权限')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Student(BaseModel):
    """学生模型类"""
    user = models.OneToOneField(User, verbose_name='所属账户', on_delete=models.CASCADE)
    major = models.CharField(max_length=50, verbose_name='专业')
    school = models.CharField(max_length=50, verbose_name='学校')
    to_time = models.DateTimeField(verbose_name='在校时间')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name


class Enterprise(BaseModel):
    """企业模型类"""
    user = models.OneToOneField(User, verbose_name='所属账户', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='企业名称')
    abstract = models.CharField(max_length=100, verbose_name='简介')
    to_time = models.DateTimeField(verbose_name='到期时间')

    class Meta:
        verbose_name = '企业'
        verbose_name_plural = verbose_name


class Tasks(object):
    pass


class UserInfo(object):
    pass
