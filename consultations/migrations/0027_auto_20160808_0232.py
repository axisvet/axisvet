# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 23:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0026_remove_item_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinicalnotes',
            old_name='clinicalnotes',
            new_name='clinical_notes',
        ),
        migrations.RenameField(
            model_name='consultation',
            old_name='arrivaltime',
            new_name='arrival_time',
        ),
        migrations.RenameField(
            model_name='consultation',
            old_name='finishtime',
            new_name='finish_time',
        ),
        migrations.RenameField(
            model_name='consultation',
            old_name='starttime',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='treatmentplan',
            old_name='treatmentplan',
            new_name='treatment_plan',
        ),
    ]