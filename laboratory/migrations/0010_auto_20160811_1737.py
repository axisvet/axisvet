# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0009_auto_20160811_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newthing',
            name='name',
        ),
        migrations.AlterField(
            model_name='laboratorypanel',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
        migrations.DeleteModel(
            name='newthing',
        ),
    ]
