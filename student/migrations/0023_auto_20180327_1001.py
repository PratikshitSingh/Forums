# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-27 04:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20180326_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mess',
            name='hostel',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 10, 1, 7, 474264)),
        ),
        migrations.DeleteModel(
            name='Mess',
        ),
    ]