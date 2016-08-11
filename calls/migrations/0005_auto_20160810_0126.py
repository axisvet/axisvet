# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_auto_20160809_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='caller_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='XXcaller_type_object_fk', to='calls.Object'),
        ),
        migrations.AlterField(
            model_name='call',
            name='receiver_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='XXreceiver_type_object_fk', to='calls.Object'),
        ),
    ]