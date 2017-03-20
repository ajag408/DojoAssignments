# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='R_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='book_review',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='book_review',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Book_Review',
        ),
        migrations.AddField(
            model_name='r_content',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Review'),
        ),
    ]
