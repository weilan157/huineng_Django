# _*_ coding:utf-8 _*_
# 作者:
# 时间:2019/5/2/20:36
import xadmin
# from mptt.admin import MPTTModelAdmin

from .models import Comment
# Register your models here.


class MPTTModelAdmin(object):
    # 列表显示
    # list_display = ['user', 'content', 'created', 'content_object', 'content_type', 'object_id']
    pass


xadmin.site.register(Comment, MPTTModelAdmin)
