# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20180220_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 20, 22, 37, 21, 716703)),
        ),
    ]
