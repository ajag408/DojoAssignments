from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class LeadManager(models.Manager):
    def isValid(self, postData):
        if postData['first_name'] == '' or postData['last_name'] == '' or postData['email'] == '' or not EMAIL_REGEX.match(postData['email']):
            return False
        else:
            return True
class Lead(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    registered_datetime = models.DateTimeField(auto_now_add = True)
    email = models.CharField(max_length = 255)
    objects = LeadManager()
