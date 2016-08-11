# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_remove_basket_callid'),
        ('calls', '0007_auto_20160810_0129'),
    ]

    operations = [
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
