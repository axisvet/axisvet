# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_laboratoryanalysisunit_panel_paneltest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaboratoryAnalysisUnit',
            new_name='LabUnit',
        ),
    ]