# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-14 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSale', '0009_auto_20190413_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produk',
            old_name='status',
            new_name='stock',
        ),
        migrations.AddField(
            model_name='produk',
            name='toko',
            field=models.CharField(default='Tokopedia', max_length=255),
        ),
    ]
