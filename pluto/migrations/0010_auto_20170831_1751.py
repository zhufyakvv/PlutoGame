# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-31 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pluto', '0009_auto_20170831_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='points',
            new_name='score',
        ),
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
