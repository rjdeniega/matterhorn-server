# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0027_program_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academicyear', to='institutions.AcademicYear'),
        ),
    ]