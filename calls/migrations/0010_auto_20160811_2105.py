# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('calls', '0009_auto_20160811_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caller_id', models.PositiveIntegerField(blank=True, null=True)),
                ('receiver_id', models.PositiveIntegerField(blank=True, null=True)),
                ('caller_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caller_type', to='contenttypes.ContentType')),
                ('receiver_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_type', to='contenttypes.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='call',
            name='caller_type',
        ),
        migrations.RemoveField(
            model_name='call',
            name='receiver_type',
        ),
        migrations.DeleteModel(
            name='Call',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
    ]
