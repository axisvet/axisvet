# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0006_auto_20160813_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paneltestrange',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.PanelTest'),
        ),
    ]
