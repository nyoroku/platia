# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2022-04-12 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premise', '0002_auto_20220412_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
