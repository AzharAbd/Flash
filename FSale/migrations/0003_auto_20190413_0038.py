# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSale', '0002_auto_20190412_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='brpice',
            field=models.CharField(default='210.000', max_length=50),
        ),
    ]
