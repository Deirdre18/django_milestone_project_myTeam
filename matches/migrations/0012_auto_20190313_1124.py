# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0011_auto_20190313_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitytable',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player_detail', to='profile_and_stats.UserProfileData'),
        ),
    ]