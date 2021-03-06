# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-11 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_stats', '0005_attributerating_last_updated'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_donation', models.DateField(auto_now_add=True)),
                ('donation_amount_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('donated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_and_stats.UserProfileData')),
            ],
        ),
    ]
