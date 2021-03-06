# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0010_auto_20160205_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enrolment',
            name='student',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='course',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='module',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='section',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='student',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='completed_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Enrolment',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
    ]
