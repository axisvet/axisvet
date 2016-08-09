# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0022_auto_20160807_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='type',
            new_name='typex',
        ),
        migrations.AlterField(
            model_name='item',
            name='typex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.ItemType'),
        ),
    ]
