# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-06 13:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 6, 16, 8, 15, 726433), verbose_name='Опубликована'),
        ),
    ]