# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20160808_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('gender', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.PatientGender'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
