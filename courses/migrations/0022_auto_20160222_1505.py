# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_auto_20160222_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='question',
            name='students',
        ),
    ]
