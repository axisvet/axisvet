# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0015_auto_20160807_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_i_type_code', to='items.ItemType'),
        ),
    ]
