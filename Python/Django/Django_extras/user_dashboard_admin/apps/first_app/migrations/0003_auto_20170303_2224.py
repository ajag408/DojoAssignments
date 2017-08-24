# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_user_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commenter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('postman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.User')),
                ('wall_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wall_posts', to='first_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_comments', to='first_app.Message'),
        ),
    ]
