# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networktoken', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='purpose',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
