# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170503_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
