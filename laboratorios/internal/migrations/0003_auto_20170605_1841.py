# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0002_auto_20170604_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('essay_methods', models.ManyToManyField(related_name='laboratories', to='internal.EssayMethod')),
            ],
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='essay_methods',
        ),
        migrations.AddField(
            model_name='essay',
            name='essay_methods',
            field=models.ManyToManyField(related_name='essays', to='internal.EssayMethod'),
        ),
        migrations.AddField(
            model_name='laboratory',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='internal.LaboratoryType'),
            preserve_default=False,
        ),
    ]