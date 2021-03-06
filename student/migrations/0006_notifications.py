# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-19 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_registration_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('message', models.CharField(max_length=500)),
                ('is_new', models.BooleanField(default=False)),
                ('time_stamp', models.TimeField()),
            ],
        ),
    ]
