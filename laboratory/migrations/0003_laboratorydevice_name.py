# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0002_auto_20160811_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorydevice',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
