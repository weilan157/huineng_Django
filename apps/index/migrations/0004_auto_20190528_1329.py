# Generated by Django 2.1.7 on 2019-05-28 13:29

import apps.index.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190503_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='image',
            field=models.ImageField(default='image/1508679309367.jpg', upload_to=apps.index.models.upload_directory_path, verbose_name='任务描述图片'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='发布用户'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='任务酬金'),
        ),
    ]
