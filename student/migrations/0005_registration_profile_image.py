# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-13 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20180211_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='profile_image',
            field=models.ImageField(default='media/34AD2.jpg', upload_to='media'),
        ),
    ]