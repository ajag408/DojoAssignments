from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validateName(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

    if value.isalpha() is False:
        raise ValidationError(
            'letters only'
        )

def validatePass(value):
    if len(value)<8:
        raise ValidationError(
            'password must be longer than 8 chars'
        )

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 45, validators = [validateName])
    last_name = models.CharField(max_length = 45, validators = [validateName])
    email = models.CharField(max_length = 255, validators = [validate_email])
    password = models.CharField(max_length = 50, validators = [validatePass])
    confirm_password = models.CharField(max_length = 50)
