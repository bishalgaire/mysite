# Generated by Django 2.0.5 on 2018-05-23 13:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180523_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
