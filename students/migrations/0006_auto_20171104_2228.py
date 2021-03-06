# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20171104_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=64),
            preserve_default=False,
        ),
    ]
