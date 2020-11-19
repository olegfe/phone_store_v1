# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-13 12:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20201113_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 13, 15, 46, 37, 266813), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 13, 15, 46, 37, 267811), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 13, 15, 46, 37, 268806), verbose_name='Дата'),
        ),
    ]