# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 09:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0023_bookcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('video_description', models.CharField(max_length=10000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('video_publish_date', models.DateField()),
                ('video_url', models.URLField(max_length=2000)),
                ('video_image_url', models.URLField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Category')),
                ('recommended_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.SubCategory')),
            ],
        ),
    ]