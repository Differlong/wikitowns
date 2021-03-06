# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20170419_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrecommendation',
            name='book_author',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookrecommendation',
            name='book_description',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookrecommendation',
            name='book_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookrecommendation',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
