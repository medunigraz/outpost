# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0016_auto_20171122_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recording',
            options={'ordering': ('-created',), 'permissions': (('view_recording', 'View Recording'),)},
        ),
    ]
