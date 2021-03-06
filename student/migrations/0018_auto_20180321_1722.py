# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20180321_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel_committee',
            name='profile_image',
            field=models.ImageField(default='default_dp.png', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 17, 22, 19, 207482)),
        ),
        migrations.AlterField(
            model_name='warden',
            name='profile_photo',
            field=models.ImageField(default='default_dp.png', upload_to='media'),
        ),
    ]
