# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0023_auto_20190408_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='reminder_emails',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True),
        ),
    ]