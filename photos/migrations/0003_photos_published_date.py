# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20170707_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
