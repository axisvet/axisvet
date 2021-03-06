# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0038_delete_itemtype'),
        ('labs', '0002_auto_20160813_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryAnalysisUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Panel',
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
        migrations.CreateModel(
            name='PanelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30)),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.Panel')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.LaboratoryAnalysisUnit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
