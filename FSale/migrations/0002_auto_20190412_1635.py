# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSale', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='deskripsi',
        ),
        migrations.AddField(
            model_name='produk',
            name='aprice',
            field=models.CharField(default='150.000', max_length=50),
        ),
        migrations.AddField(
            model_name='produk',
            name='brpice',
            field=models.CharField(default='150.000', max_length=50),
        ),
        migrations.AddField(
            model_name='produk',
            name='img',
            field=models.CharField(default='img/product/p1.jpg', max_length=255),
        ),
        migrations.AddField(
            model_name='produk',
            name='status',
            field=models.CharField(default='Terjual sebagian', max_length=50),
        ),
    ]
