# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 10:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20180321_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel_Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=10)),
                ('profile_image', models.ImageField(default='media/default_dp.png', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Hostel_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_number', models.IntegerField()),
                ('mess_maharaja', models.CharField(max_length=300)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Hostel_name')),
            ],
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warden_name', models.CharField(max_length=500)),
                ('contact_number', models.CharField(max_length=10)),
                ('profile_photo', models.ImageField(default='media/default_dp.png', upload_to='media')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Hostel_name')),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='message',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 16, 21, 56, 935736)),
        ),
        migrations.AddField(
            model_name='hostel_committee',
            name='hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Hostel_name'),
        ),
    ]
