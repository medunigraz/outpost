# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-30 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def forwards(apps, schema_editor):
    Edge = apps.get_model('geo', 'Edge')
    EdgeCategory = apps.get_model('geo', 'EdgeCategory')
    default = EdgeCategory.objects.create(name='Standard', weight=1.0)
    Edge.objects.all().update(category=default)


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0011_auto_20170619_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='EdgeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('weight', models.DecimalField(decimal_places=1, default=1.0, max_digits=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='edge',
            name='weight',
        ),
        migrations.AddField(
            model_name='edge',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='geo.EdgeCategory', null=True),
        ),
        migrations.RunPython(forwards, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='edge',
            name='category',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.CASCADE, to='geo.EdgeCategory'),
        )
    ]
