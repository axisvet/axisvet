# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0032_auto_20160811_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='special_procedure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.SpecialProcedure'),
        ),
    ]
