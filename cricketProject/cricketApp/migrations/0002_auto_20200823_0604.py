# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-08-23 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_winner',
            field=models.CharField(blank=True, choices=[('team1', 'Team1'), ('team2', 'Team2')], max_length=15, null=True, verbose_name='Winner of the match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='profile_picture',
            field=models.ImageField(max_length=255, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo_uri',
            field=models.ImageField(max_length=255, upload_to='team_logo/'),
        ),
    ]