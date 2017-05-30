# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0004_auto_20170527_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='laboratory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internal.Laboratory'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
