# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0017_auto_20170829_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterestinstance',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
