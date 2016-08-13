# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0038_delete_itemtype'),
        ('laboratory', '0018_auto_20160812_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
