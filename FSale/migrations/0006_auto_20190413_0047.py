# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 00:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FSale', '0005_auto_20190413_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produk',
            old_name='aprice',
            new_name='after_price',
        ),
        migrations.RenameField(
            model_name='produk',
            old_name='brpice',
            new_name='before_price',
        ),
    ]
