from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured
# Create your views here.
class Main(object):
    template = ''
    context = None
    favorite_number = None
    least_favorite_number = None
    def get(self, request):
        context = {'sum': self.add(self.favorite_number, self.least_favorite_number),
                    'difference': self.subtract(self.favorite_number, self.least_favorite_number),
                    'product': self.multiply(self.favorite_number, self.least_favorite_number),
                    'factor': self.divide(self.favorite_number, self.least_favorite_number)}
        return render(request, self.get_template(), context)
    def get_template(self):
        if self.template == '':
            raise ImproperlyConfigured('Template not defined')
        return self.template
    def add(self, num1, num2):
        return num1+num2
    def subtract(self, num1, num2):
        return num1-num2
    def multiply(self, num1, num2):
        return num1*num2
    def divide(self, num1, num2):
        return num1/num2

class Calculator(Main, View):
    template = 'calcApp/index.html'
    favorite_number = 7
    least_favorite_number = 20
    # sum1 = self.add(favorite_number, least_favorite_number)
    # difference = self.subtract(favorite_number, least_favorite_number)
    # product = self.multiply(favorite_number, least_favorite_number)
    # factor = self.divide(favorite_number, least_favorite_number)
