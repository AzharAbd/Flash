# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSale', '0008_produk_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]