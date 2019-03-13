# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0010_auto_20190313_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitytable',
            name='matchID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='matches.MatchData'),
        ),
    ]
