# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post_q', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]