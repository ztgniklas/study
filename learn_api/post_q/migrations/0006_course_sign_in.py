# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_q', '0005_auto_20170426_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sign_in',
            field=models.BooleanField(default=False),
        ),
    ]
