# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_auto_20160809_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caller',
            new_name='Object',
        ),
        migrations.RemoveField(
            model_name='call',
            name='Receiver',
        ),
        migrations.RemoveField(
            model_name='call',
            name='caller_type_id',
        ),
        migrations.AddField(
            model_name='call',
            name='caller_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='caller_type_object_fk', to='calls.Object'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='call',
            name='receiver_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='call',
            name='receiver_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_type_object_fk', to='calls.Object'),
            preserve_default=False,
        ),
    ]
