# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-27 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_subcategory_subcategory_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_img',
            field=models.ImageField(null=True, upload_to='subcategory_images'),
        ),
    ]
