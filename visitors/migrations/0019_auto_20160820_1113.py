# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 08:13
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0018_auto_20160820_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='client',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='client', chained_model_field='client', on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='visitors.Client'),
        ),
    ]