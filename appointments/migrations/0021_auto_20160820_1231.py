# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 09:31
from __future__ import unicode_literals

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0020_remove_appointment_practice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patients',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='client', chained_model_field='client', to='visitors.Patient'),
        ),
    ]
