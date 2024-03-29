# Generated by Django 2.1.7 on 2019-04-25 11:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=6, verbose_name='标签')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Examine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_examine', models.CharField(choices=[('待审核', '未审核'), ('已审核', '已审核'), ('未通过', '未通过')], default='待审核', max_length=6, verbose_name='审核状态')),
                ('num_examine', models.IntegerField(default=0, verbose_name='审核次数')),
            ],
            options={
                'verbose_name': '审核',
                'verbose_name_plural': '审核',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=20, verbose_name='任务标题')),
                ('describe', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='任务内容')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='任务金额')),
                ('to_time', models.DateTimeField(verbose_name='截至时间')),
                ('num', models.IntegerField(default=0, verbose_name='访问量')),
                ('num_max', models.IntegerField(default=10, verbose_name='发布上限')),
                ('receive_name', models.IntegerField(default=0, verbose_name='领取人')),
                ('image', models.ImageField(blank=True, default='image/1508679309367.jpg', null=True, upload_to='image/%Y/%m', verbose_name='任务描述图片')),
                ('is_receive', models.CharField(choices=[('待接取', '待接取'), ('待完成', '待完成'), ('已完成', '已完成')], default='待接取', max_length=6, verbose_name='任务状态')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
    ]
