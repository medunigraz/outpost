# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusonline', '0019_pers_typo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletin',
            options={'managed': False, 'ordering': ('-published',)},
        ),
    ]