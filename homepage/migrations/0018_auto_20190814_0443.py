# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-14 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20190809_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttemplate',
            name='catalogBG1',
            field=models.ImageField(null=True, upload_to=homepage.models.getPImageAttachment),
        ),
        migrations.AddField(
            model_name='producttemplate',
            name='catalogBG2',
            field=models.ImageField(null=True, upload_to=homepage.models.getPImageAttachment),
        ),
        migrations.AddField(
            model_name='producttemplate',
            name='rteDescription',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
