# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='object_id',
            field=models.CharField(max_length=36),
        ),
    ]