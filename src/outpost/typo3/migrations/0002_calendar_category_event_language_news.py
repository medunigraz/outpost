# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-10 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('typo3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'typo3_calendar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('marker', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'typo3_category',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('allday', models.BooleanField()),
                ('title', models.TextField(blank=True, null=True)),
                ('organizer', models.CharField(blank=True, max_length=256, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('teaser', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('register', models.BooleanField()),
                ('registration_end', models.DateTimeField(blank=True, null=True)),
                ('attending_fees', models.BooleanField()),
                ('url', models.CharField(blank=True, max_length=512, null=True)),
                ('dfp_points', models.IntegerField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('target', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'typo3_event',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('flag', models.CharField(blank=True, max_length=2, null=True)),
                ('isocode', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'typo3_language',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('teaser', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('tags', models.IntegerField(blank=True, null=True)),
                ('topnews', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'typo3_news',
            },
        ),
    ]
