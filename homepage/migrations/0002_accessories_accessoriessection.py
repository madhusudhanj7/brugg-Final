# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('mainImage', models.ImageField(null=True, upload_to=homepage.models.getaccessImageAttachment)),
                ('sectionImage', models.ImageField(null=True, upload_to=homepage.models.getaccessImageAttachment)),
            ],
        ),
        migrations.CreateModel(
            name='AccessoriesSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=200, null=True)),
                ('desc1', models.TextField(max_length=5000, null=True)),
                ('title2', models.CharField(max_length=200, null=True)),
                ('desc2', models.TextField(max_length=500, null=True)),
                ('lang', models.CharField(max_length=200, null=True)),
                ('accessories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessSections', to='homepage.Accessories')),
            ],
        ),
    ]
