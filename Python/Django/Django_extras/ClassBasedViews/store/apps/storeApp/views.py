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

class Edit(View):
    def get(self, request, id):
        context = {
            'product': Product.objects.get(id = id),
            'manufacturers': Manufacturer.objects.all()
        }
        return render(request, 'storeApp/product.html', context)
    def post(self, request, id):
        isValid = Product.objects.isValid(request.POST)
        print isValid
        if isValid is True:
            print 'valid'
            product = Product.objects.get(id = id)
            manufacturer = Manufacturer.objects.get(name=request.POST['manufacturer'])
            product.manufacturer = manufacturer
            product.name = request.POST['name']
            product.price = int(request.POST['price'])
            product.description = request.POST['description']
            product.save()
        return redirect('/products/' + id)

def delete(request, id):
    p = Product.objects.get(id=id)
    p.delete()
    return redirect('/products')
