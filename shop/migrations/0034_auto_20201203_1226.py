# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-03 09:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20201203_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='weigth',
            new_name='weight',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 3, 12, 26, 14, 923493), verbose_name='Дата'),
        ),
    ]
