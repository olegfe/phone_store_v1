# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-01 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20201201_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 1, 16, 50, 53, 301238), verbose_name='Дата'),
        ),
    ]
