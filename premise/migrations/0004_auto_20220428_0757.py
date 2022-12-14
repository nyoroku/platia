# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2022-04-28 04:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import phonenumber_field.modelfields
import smart_selects.db_fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('premise', '0003_auto_20220412_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('photo', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='attractions')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='business', max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('location', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created', models.DateTimeField(auto_now=True)),
                ('tag_line', models.CharField(max_length=100)),
                ('photo', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='attractions')),
                ('categories', models.ManyToManyField(blank=True, related_name='categories', to='premise.Category')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premise.County')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premise.County')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='ward',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='county', chained_model_field='county', on_delete=django.db.models.deletion.CASCADE, to='premise.Ward'),
        ),
    ]
