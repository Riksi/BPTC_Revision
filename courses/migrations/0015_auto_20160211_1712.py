# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_remove_section_completed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='section',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='student',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
    ]