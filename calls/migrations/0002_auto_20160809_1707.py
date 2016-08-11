# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='call',
            name='CallerName',
        ),
        migrations.AddField(
            model_name='call',
            name='caller_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='call',
            name='Receiver',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='call',
            name='caller_type_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='call_caller_fk', to='calls.Caller'),
            preserve_default=False,
        ),
    ]