# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='processor',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
