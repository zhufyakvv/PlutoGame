# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pluto', '0008_auto_20170831_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='hero_dir',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='hero_x',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='hero_y',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
