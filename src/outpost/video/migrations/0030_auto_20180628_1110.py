# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0029_polymorphic_ctype_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epiphansource',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='epiphansource',
            name='video',
        ),
    ]
