# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scorers', '0002_auto_20171021_2324'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='league',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='league',
            name='district',
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
        migrations.DeleteModel(
            name='League',
        ),
    ]
