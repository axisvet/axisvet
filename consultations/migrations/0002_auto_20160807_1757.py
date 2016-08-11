# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20160807_1757'),
        ('consultations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='type_code',
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_i_type_code', to='items.ItemType'),
        ),
    ]