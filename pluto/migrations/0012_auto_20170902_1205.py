# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-02 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pluto', '0011_auto_20170831_1754'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Result',
            new_name='Record',
        ),
    ]
