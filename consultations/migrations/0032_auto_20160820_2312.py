# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0031_auto_20160820_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='arrival_time',
        ),
        migrations.AlterField(
            model_name='consultation',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
