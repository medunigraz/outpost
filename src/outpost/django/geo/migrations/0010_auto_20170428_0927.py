# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 07:27
from __future__ import unicode_literals

from django.db import migrations
from ...base.fields import LowerCaseCharField


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0009_remove_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='color',
            field=LowerCaseCharField(default='007b3c', max_length=6),
        ),
    ]
