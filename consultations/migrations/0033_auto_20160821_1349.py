# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0032_auto_20160820_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='finish_time',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='start_time',
        ),
    ]
