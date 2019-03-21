# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_stats', '0002_auto_20190309_1352'),
        ('matches', '0013_auto_20190313_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availabilitytable',
            options={'ordering': ('matchID', 'status', 'player')},
        ),
        migrations.RemoveField(
            model_name='availabilitytable',
            name='player',
        ),
        migrations.AddField(
            model_name='availabilitytable',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='profile_and_stats.UserProfileData'),
            preserve_default=False,
        ),
    ]