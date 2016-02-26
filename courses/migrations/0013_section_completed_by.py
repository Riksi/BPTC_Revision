# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0012_auto_20160211_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='completed_by',
            field=models.ManyToManyField(through='courses.Progress', to=settings.AUTH_USER_MODEL),
        ),
    ]
