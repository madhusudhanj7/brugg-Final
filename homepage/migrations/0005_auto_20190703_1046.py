# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20190703_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoriessection',
            name='categoryName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='accessoriessection',
            name='productName',
            field=models.CharField(max_length=200),
        ),
    ]