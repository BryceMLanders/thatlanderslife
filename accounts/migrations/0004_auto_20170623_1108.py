# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='follows',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nickname',
        ),
    ]