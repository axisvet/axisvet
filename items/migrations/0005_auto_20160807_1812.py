# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20160807_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='costprice',
            new_name='cost_price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='saleprice',
            new_name='sale_price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='salepricevatrate',
            new_name='sale_price_vat_rate',
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.ItemType'),
        ),
    ]