# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-29 20:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20170727_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 29, 20, 37, 28, 882760)),
        ),
    ]
