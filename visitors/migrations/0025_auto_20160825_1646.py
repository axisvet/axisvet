# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0024_auto_20160823_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='county',
            field=models.CharField(blank=True, max_length=30, verbose_name='County / State'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='organisation_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='visitors.Client', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='colour',
            field=models.CharField(blank=True, max_length=30, verbose_name='Colour / Markings'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('female sterilised', 'Female Sterilised'), ('male', 'Male'), ('male sterilised', 'Male Sterilised'), ('unknown', 'Unknown')], max_length=50, verbose_name='Male / Female'),
        ),
    ]
