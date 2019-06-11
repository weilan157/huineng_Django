from .models import Tasks, Examine, Classify
import xadmin


class TasksAdmin(object):
    # 列表显示
    list_display = ['owner', 'title', 'picker',
                    'price', 'image', 'to_time', 'num', 'receive_name',
                    # 'num_examine',  # 'is_receive',
                    'create_time', 'update_time']
    # 搜索字段 不要添加时间
    search_fields = ['owner', 'title', 'picker',
                     'price', 'num',  # 'is_receive', 'num_examine',
                     'receive_name', ' num_max']
    # 过滤器
    list_filter = ['owner', 'title', 'is_default',
                   'price', 'to_time', 'num',
                   # 'num_examine',  # 'is_receive',
                   'create_time', 'update_time', 'is_delete']

    # 配置默认排序规则
    # ordering = ['-people_nums']
    # 设置未只读，不能修改
    # readonly_fields = ['proplr_nums']
    # 设置为后台不能看见,与readony_fields冲突，有前者，exclude不生效
    # exclude = ['fav_nums']
    # 设置添加时可以搜索，而不是下拉框，ajax加载(外键)
    # relfield_style = 'fk-ajax'
    # 在同一个页面添加完整数据,不可以在嵌套中嵌套，但可以多个，同一个model注册两个管理器
    # inlines = [LessonInline, CourseResourceInline]
    # 列表页直接修改的字段
    # list_editable = ['degree', 'desc']


class ExamineAdmin(object):

    list_display = ["is_examine", "num_examine"]
    search_fields = ["is_examine", "num_examine"]


class ClassifyAdmin(object):

    list_display = ["owner", "label"]
    search_fields = ["owner", "label"]


xadmin.site.register(Tasks, TasksAdmin)
xadmin.site.register(Examine, ExamineAdmin)
xadmin.site.register(Classify, ClassifyAdmin)
