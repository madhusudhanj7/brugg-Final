# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-05 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0026_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='representation',
            field=models.BooleanField(default=False),
        ),
    ]
