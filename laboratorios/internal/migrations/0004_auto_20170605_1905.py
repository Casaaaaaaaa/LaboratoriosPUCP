# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_auto_20170605_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorytype',
            name='essay_methods',
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='type',
        ),
        migrations.AddField(
            model_name='laboratory',
            name='essay_methods',
            field=models.ManyToManyField(related_name='laboratories', to='internal.EssayMethod'),
        ),
        migrations.DeleteModel(
            name='LaboratoryType',
        ),
    ]