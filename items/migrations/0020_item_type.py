# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0019_remove_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.ItemType'),
            preserve_default=False,
        ),
    ]
