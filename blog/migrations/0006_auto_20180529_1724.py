# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-29 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180529_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='ano',
            field=models.IntegerField(max_length=4),
        ),
    ]
