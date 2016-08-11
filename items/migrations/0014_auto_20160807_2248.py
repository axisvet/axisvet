# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_location'),
        ('items', '0013_auto_20160807_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('total_dispensing_units_in_package', models.IntegerField(default=0)),
                ('controlled_substance', models.BooleanField(default=False)),
                ('vaccine', models.BooleanField(default=False)),
                ('dispensing_unit', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.Unit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='controlled_substance',
        ),
        migrations.RemoveField(
            model_name='item',
            name='dispensing_unit',
        ),
        migrations.RemoveField(
            model_name='item',
            name='location',
        ),
        migrations.RemoveField(
            model_name='item',
            name='package_type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='total_dispensing_units_in_package',
        ),
        migrations.RemoveField(
            model_name='item',
            name='vaccine',
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.ItemType'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.Location'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='package_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='items.Package'),
        ),
    ]