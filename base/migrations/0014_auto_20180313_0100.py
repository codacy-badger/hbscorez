# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-13 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20180313_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportshall',
            name='phone_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]