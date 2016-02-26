# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0020_auto_20160222_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='question',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='student',
        ),
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
