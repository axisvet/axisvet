# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0003_auto_20160809_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='object_code',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='object_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
