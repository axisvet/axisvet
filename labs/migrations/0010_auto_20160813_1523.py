# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0011_auto_20160812_2233'),
        ('items', '0038_delete_itemtype'),
        ('labs', '0009_auto_20160813_1514'),
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
        migrations.CreateModel(
            name='AnalysisRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('min', models.DecimalField(decimal_places=2, max_digits=6)),
                ('max', models.DecimalField(decimal_places=2, max_digits=6)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labs.Analysis')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.Species')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='analysisreference',
            name='species',
        ),
        migrations.RenameField(
            model_name='paneltestrange',
            old_name='ggg',
            new_name='panel',
        ),
        migrations.DeleteModel(
            name='AnalysisReference',
        ),
    ]