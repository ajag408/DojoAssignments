from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate(self, email):
        
        if EMAIL_REGEX.match(email):

            User.objects.create(email=email)
            return True

        else:

            return False


class User(models.Model):
    email = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()
