# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='section',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
