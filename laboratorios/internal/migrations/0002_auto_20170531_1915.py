# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtemplate',
            name='essay_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='internal.EssayTemplate'),
        ),
    ]