# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 08:31
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campusonline', '0009_course_coursegroup_coursegroupterm_student'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='student',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='terminal',
            name='campusonline',
        ),
        migrations.AddField(
            model_name='terminal',
            name='room',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='campusonline.Room'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='room',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='campusonline.Room'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='student',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='campusonline.Student'),
        ),
        migrations.AlterField(
            model_name='holding',
            name='lecturer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='campusonline.Person'),
        ),
        migrations.AlterField(
            model_name='terminal',
            name='config',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
