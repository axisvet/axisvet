# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 19:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0011_remove_appointment_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='a_u_createdby', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
