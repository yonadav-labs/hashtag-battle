# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0002_remove_battle_compare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='avg_length1',
            field=models.FloatField(default=0, help_text='Average Length of tweets with hashtag1, Bigger is winner.'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='avg_length2',
            field=models.FloatField(default=0, help_text='Average Length of tweets with hashtag2'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='end_time',
            field=models.DateTimeField(help_text='Format: YYYY-MM-DD hh:mm:ss'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='frequency1',
            field=models.FloatField(default=0, help_text='Frequency of tweets with hashtag1 (number of tweets per second), Bigger is winner.'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='frequency2',
            field=models.FloatField(default=0, help_text='Frequency of tweets with hashtag2'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='name',
            field=models.CharField(help_text='Battle Name', max_length=250),
        ),
        migrations.AlterField(
            model_name='battle',
            name='num_typo1',
            field=models.IntegerField(default=0, help_text='Number of typos in tweets with hashtag1, Smaller is winner.'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='num_typo2',
            field=models.IntegerField(default=0, help_text='Number of typos in tweets with hashtag2'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='start_time',
            field=models.DateTimeField(help_text='Format: YYYY-MM-DD hh:mm:ss'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='tag1',
            field=models.CharField(help_text='Hashtag 1 - no # sign, no space', max_length=250),
        ),
        migrations.AlterField(
            model_name='battle',
            name='tag2',
            field=models.CharField(help_text='Hashtag 2', max_length=250),
        ),
    ]
