# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 00:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20170831_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 0, 14, 55, 723506)),
        ),
    ]
