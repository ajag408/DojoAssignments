from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NoteManager(models.Manager):
    def isValid(self,postData):
        if len(postData['title']) == 0:
            return False
        else:
            return True
class Note(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    objects = NoteManager()
