# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-06 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0032_auto_20190906_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='shortUrl',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
