# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 16:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0030_auto_20160821_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment', 'verbose_name_plural': 'Appointments'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='attending_staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vet/Nurse'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.Client', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='consultation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_con', to='consultations.Consultation', verbose_name='Consultation'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='duration',
            field=models.IntegerField(verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last updated by'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patients',
            field=smart_selects.db_fields.ChainedManyToManyField(auto_choose=True, chained_field='client', chained_model_field='client', to='visitors.Patient', verbose_name='Animals'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.CharField(max_length=500, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start',
            field=models.DateTimeField(verbose_name='Date/Time'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('arrived', 'Arrived'), ('in consult', 'In Consult'), ('waiting to pay', 'Waiting to Pay'), ('payment complete', 'Payment Complete')], max_length=50, verbose_name='Status'),
        ),
    ]