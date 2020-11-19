# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-19 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201019_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='accum_volume',
            field=models.CharField(default=0, max_length=255, verbose_name='Объем батареи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='frontal_cam_mp',
            field=models.CharField(default=0, max_length=255, verbose_name='Фронтальная камера'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='main_cam_mp',
            field=models.CharField(default=0, max_length=255, verbose_name='Фронтальная камера'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(default=0, max_length=255, verbose_name='Оперативная память'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AddField(
            model_name='product',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем SD карты'),
        ),
    ]
