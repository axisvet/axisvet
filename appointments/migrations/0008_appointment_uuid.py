# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_remove_appointment_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
