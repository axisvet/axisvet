# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]