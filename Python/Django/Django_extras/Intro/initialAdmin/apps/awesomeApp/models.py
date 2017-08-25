from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 255)

class Fruit(models.Model):
    name = models.CharField(max_length = 255)

class Donut(models.Model):
    name = models.CharField(max_length = 255)

class Group(models.Model):
    name = models.CharField(max_length = 255)
