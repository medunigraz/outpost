# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 08:57
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networktoken', '0006_radius_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='lifetime',
            field=models.DurationField(default=datetime.timedelta(0, 21600), validators=[django.core.validators.MaxValueValidator(datetime.timedelta(1)), django.core.validators.MinValueValidator(datetime.timedelta(0, 3600))]),
        ),
    ]
