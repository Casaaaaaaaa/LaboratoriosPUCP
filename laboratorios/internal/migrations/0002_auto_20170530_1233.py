# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essayfill',
            name='description',
            field=models.CharField(default='essay testing', max_length=100),
        ),
        migrations.AlterField(
            model_name='parameterfill',
            name='value',
            field=models.CharField(default='Empty field', max_length=100),
        ),
        migrations.AlterField(
            model_name='testfill',
            name='description',
            field=models.CharField(default='descripcion', max_length=100),
        ),
    ]
