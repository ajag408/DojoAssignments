# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 04:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_auto_20170831_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='sprite',
            field=models.FileField(default=1, upload_to='static/first_app/img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 4, 14, 56, 806951)),
        ),
    ]
