from __future__ import unicode_literals

from django.db import models

class ProductManager(models.Manager):
    def isValid(self, postData):
        if len(postData['name']) == 0 or len(postData['price']) == 0 or len(postData['description']) == 0:
            return False
        elif len(postData['name']) < 8:
            return False
        elif postData['price'] == 0:
            return False
        elif len(postData['description']) > 50:
            return False
        else:
            return True

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length = 50)
    def __repr__(self):
        return "<Manufacturer object: {}>".format(self.name)

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name = 'products')
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = ProductManager()
    def __repr__(self):
        return "<Product object: {} {} {}>".format(self.manufacturer, self.name, self.price)
