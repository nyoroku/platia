# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-01 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('course', models.CharField(max_length=80)),
                ('qualification', models.CharField(default='N/A', max_length=20, verbose_name='academic qualification')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('applied', models.DateTimeField(auto_now_add=True, verbose_name='applied on')),
                ('aboutus', models.TextField(blank=True, verbose_name='how did you find out about us?')),
            ],
            options={
                'ordering': ('-applied',),
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('author', models.CharField(max_length=200)),
                ('overview', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Latest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='latest', unique_for_date='created')),
                ('photo', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='latest')),
                ('day', models.DateField(verbose_name='Event Day')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Events Happening',
                'verbose_name_plural': 'Events Happening',
            },
        ),
    ]
