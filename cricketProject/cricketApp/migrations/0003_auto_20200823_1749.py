# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-08-23 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricketApp', '0002_auto_20200823_0604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['-match_date']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-team_points']},
        ),
    ]
