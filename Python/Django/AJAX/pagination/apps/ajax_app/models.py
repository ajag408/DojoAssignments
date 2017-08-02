from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    registered_datetime = models.DateTimeField(auto_now_add = True)
    email = models.CharField(max_length = 255)
