# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-06 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0031_locations_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='address_de',
            field=models.TextField(blank=True, max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='address_en',
            field=models.TextField(blank=True, max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='address_zh',
            field=models.TextField(blank=True, max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
