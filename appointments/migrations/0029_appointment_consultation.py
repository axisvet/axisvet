# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0035_auto_20160821_1400'),
        ('appointments', '0028_auto_20160820_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='consultation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultations.Consultation'),
        ),
    ]
