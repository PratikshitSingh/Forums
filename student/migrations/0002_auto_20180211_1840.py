# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-11 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='year',
            field=models.IntegerField(),
        ),
    ]
