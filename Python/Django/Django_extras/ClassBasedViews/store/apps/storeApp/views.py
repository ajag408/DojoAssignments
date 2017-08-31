from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.views.generic import View

# Create your views here.
def index(request):
    return redirect('/products')

class Products(View):
    def get(self, request):
        context = {
            'products': Product.objects.all(),
            'manufacturers': Manufacturer.objects.all()
        }
        return render(request, 'storeApp/products.html', context)
    def post(self, request):
        # print request.POST
        isValid = Product.objects.isValid(request.POST)
        if isValid is True:
            manufacturer = Manufacturer.objects.get(name = request.POST['manufacturer'])
            Product.objects.create(manufacturer = manufacturer, name = request.POST['name'], price = int(request.POST['price']), description = request.POST['description'])
        return redirect('/products')
