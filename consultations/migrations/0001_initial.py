# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 09:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitors', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('clinicalnotes', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('arrivaltime', models.DateTimeField()),
                ('starttime', models.DateTimeField()),
                ('finishtime', models.DateTimeField()),
                ('caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.Client')),
                ('patient', models.ManyToManyField(to='visitors.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('diagnosis', models.CharField(max_length=1000)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.Consultation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('price_with_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.Consultation')),
                ('type_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_i_type_code', to='items.Itemtype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('observation', models.CharField(max_length=1000)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.Consultation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TreatmentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('treatmentplan', models.CharField(max_length=1000)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.Consultation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='clinicalnotes',
            name='consultation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.Consultation'),
        ),
    ]
