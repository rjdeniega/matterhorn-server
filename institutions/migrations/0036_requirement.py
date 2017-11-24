# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-24 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0035_auto_20171121_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('archiver', models.CharField(blank=True, max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.OutboundProgram')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]