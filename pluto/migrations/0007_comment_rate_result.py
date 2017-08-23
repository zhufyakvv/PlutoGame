# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-23 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pluto', '0006_auto_20170822_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=256)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_by', to=settings.AUTH_USER_MODEL)),
                ('forward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_forward', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pluto.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_by', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pluto.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.TextField(max_length=512)),
                ('points', models.IntegerField()),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_by', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pluto.Level')),
            ],
        ),
    ]