# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-04 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0043_auto_20171204_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inboundstudentprogram',
            name='inbound_courses',
        ),
        migrations.AddField(
            model_name='acceptedstudentprogram',
            name='inbound_courses',
            field=models.ManyToManyField(blank=True, to='students.InboundCourse'),
        ),
    ]
