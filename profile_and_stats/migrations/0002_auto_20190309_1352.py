# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-09 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofiledata',
            options={'ordering': ('username',)},
        ),
    ]