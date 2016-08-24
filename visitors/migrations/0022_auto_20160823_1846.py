# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0021_auto_20160820_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name': 'Species', 'verbose_name_plural': 'Species'},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='remark',
        ),
        migrations.AddField(
            model_name='client',
            name='county',
            field=models.CharField(blank=True, max_length=30, verbose_name='State / County'),
        ),
        migrations.AddField(
            model_name='patient',
            name='remarks',
            field=models.CharField(blank=True, max_length=200, verbose_name='Remarks'),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='Town / City'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(max_length=20, verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='organisation_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='remarks',
            field=models.CharField(blank=True, max_length=200, verbose_name='Remarks'),
        ),
        migrations.AlterField(
            model_name='client',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='street_address_2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='client',
            name='zip',
            field=models.CharField(blank=True, max_length=10, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='breed',
            field=models.CharField(blank=True, max_length=30, verbose_name='Breed'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='visitors.Client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='colour',
            field=models.CharField(blank=True, max_length=30, verbose_name='Colour'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='deceased',
            field=models.BooleanField(default=False, verbose_name='Deceased'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('female sterilised', 'Female Sterilised'), ('male', 'Male'), ('male sterilised', 'Male Sterilised'), ('unknown', 'Unknown')], max_length=50, verbose_name='Male/Female'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='microchip',
            field=models.CharField(blank=True, max_length=30, verbose_name='Microchip ID'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.Species', verbose_name='Species'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Weight (kg)'),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Species name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='species_code',
            field=models.CharField(max_length=30, verbose_name='Unique ID code'),
        ),
    ]
