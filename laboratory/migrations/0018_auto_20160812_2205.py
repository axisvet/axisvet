# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0017_auto_20160812_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panelreference',
            name='analysis',
        ),
        migrations.RemoveField(
            model_name='panelreference',
            name='unit',
        ),
        migrations.AlterField(
            model_name='panelreference',
            name='panel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.PanelTest'),
        ),
    ]
