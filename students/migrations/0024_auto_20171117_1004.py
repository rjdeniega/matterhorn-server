# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-17 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20171117_0951'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentProgram',
            new_name='StudentStudyField',
        ),
    ]
