# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_stats', '0002_auto_20190309_1352'),
        ('matches', '0005_matchdata_match_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True)),
                ('matchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.MatchData')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_and_stats.UserProfileData')),
            ],
            options={
                'ordering': ('matchID', 'status', 'player'),
            },
        ),
    ]
