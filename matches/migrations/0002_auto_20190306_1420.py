# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-06 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_status',
            field=models.CharField(choices=[('S', 'Scheduled'), ('C', 'Cancelled')], default='S', max_length=1),
        ),
    ]
