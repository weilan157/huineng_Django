# _*_ encoding:utf-8 _*_

import xadmin
from .models import Student, Enterprise
from xadmin import views


class BaseSetting(object):
    """主题功能显示"""
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """对后台管理标记信息进行命名，全局设置"""
    site_title = "会能后台管理系统"   # 后台头部信息
    site_footer = "会能网"    # 后台脚底信息
    menu_style = "accordion"  # 左侧的app相关的表是否进行抽屉式收拢


class StudentAdmin(object):
    """后台显示"""
    # 列表显示
    list_display = ['user', 'major', 'school', 'to_time']
    # 搜索字段 不要添加时间
    search_fields = ['user', 'major', 'school']
    # 过滤器
    list_filter = ['user', 'major', 'school', 'to_time']
    

class EnterpriseAdmin(object):
    """后台显示"""
    # 列表显示
    list_display = ['user', 'name', 'abstract', 'to_time']
    # 搜索字段 不要添加时间
    search_fields = ['user', 'name', 'abstract']
    # 过滤器
    list_filter = ['user', 'name', 'abstract', 'to_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Enterprise, EnterpriseAdmin)
