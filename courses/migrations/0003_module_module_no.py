# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 17:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_progress_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='module_no',
            field=models.IntegerField(default=datetime.datetime(2016, 2, 5, 17, 47, 8, 557704, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
