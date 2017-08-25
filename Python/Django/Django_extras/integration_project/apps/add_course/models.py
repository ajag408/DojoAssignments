from __future__ import unicode_literals

from django.db import models
from ..first_app.models import User
# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors['name'] = 'Course name must be at least 10 characters'
        if len(postData['description']) < 15:
            errors['description'] = 'Description must be at least 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    users = models.ManyToManyField(User)
    objects = CourseManager()
    def __repr__(self):
        return "<Course object: {}>".format(self.name)


class Description(models.Model):
    course = models.OneToOneField(Course, related_name = 'course_description')
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return "<Description object: {}>".format(self.description)

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name = 'comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Comment object: {}>".format(self.comment)
