# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0009_essaymethodfill_sample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essaymethodfill',
            name='sample',
        ),
    ]
