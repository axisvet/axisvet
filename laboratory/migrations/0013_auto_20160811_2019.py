# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0012_auto_20160811_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoryanalysisreferencevalue',
            name='max',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='laboratoryanalysisreferencevalue',
            name='min',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
