# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20170303_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(default='normal', max_length=7),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
