# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-05 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_auto_20180405_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 5, 22, 19, 28, 210983)),
        ),
    ]
