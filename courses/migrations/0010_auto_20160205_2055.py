# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20160205_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='course',
            new_name='module',
        ),
    ]
