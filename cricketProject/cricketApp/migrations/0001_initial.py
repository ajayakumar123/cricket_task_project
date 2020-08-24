# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-08-23 05:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('team1_score', models.IntegerField()),
                ('team2_score', models.IntegerField()),
                ('match_winner', models.CharField(choices=[('team1', 'Team1'), ('team2', 'Team2')], max_length=15, verbose_name='Winner of the match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profile_picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='profiles/')),
                ('jersey_number', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
                ('no_of_matches', models.IntegerField(verbose_name='No of Matches Played')),
                ('runs', models.IntegerField()),
                ('highest_score', models.IntegerField()),
                ('fifties', models.IntegerField()),
                ('hundreds', models.IntegerField()),
                ('strike_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo_uri', models.ImageField(blank=True, max_length=255, null=True, upload_to='team_logo/')),
                ('club_state', models.CharField(max_length=30)),
                ('matches_played', models.IntegerField(default=0)),
                ('matches_won', models.IntegerField(default=0)),
                ('matches_lost', models.IntegerField(default=0)),
                ('team_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', related_query_name='players', to='cricketApp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches1', related_query_name='matches1', to='cricketApp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches2', related_query_name='matches2', to='cricketApp.Team'),
        ),
    ]