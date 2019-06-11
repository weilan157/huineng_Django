# _*_ coding:utf-8 _*_
# 作者:
# 时间:2019/5/22/19:20
from haystack import indexes
from .models import Tasks, Classify


class TasksIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    def get_model(self):  # 重载get_model方法，必须要有！获取检索对应对的模型
        return Tasks

    def index_queryset(self, using=None):
        """在更新模型的整个索引时使用."""
        return self.get_model().objects.all()  # 获取所有，可以加判断


# class ClassifyIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
#     text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段
#
#     def get_model(self):  # 重载get_model方法，必须要有！获取检索对应对的模型
#         return Classify
#
#     def index_queryset(self, using=None):
#         """在更新模型的整个索引时使用."""
#         return self.get_model().objects.all()
