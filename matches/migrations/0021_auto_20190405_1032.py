# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-05 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0020_auto_20190403_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchdata',
            options={'ordering': ('-date_of_match', 'time_of_match')},
        ),
        migrations.AlterModelOptions(
            name='performancerating',
            options={'ordering': ('performance_matchID',)},
        ),
    ]