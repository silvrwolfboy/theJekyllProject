# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-09 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theJekyllProject', '0015_cname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
