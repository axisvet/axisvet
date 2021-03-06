# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20160807_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dispensing_unit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.Unit'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.ItemType'),
        ),
    ]
