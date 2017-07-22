from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'cash_spent' not in request.session:
        request.session['cash_spent'] = 0
    if 'items_ordered' not in request.session:
        request.session['items_ordered'] = 0
    return render(request, 'amadon_app/index.html')

def purchase(request, word):
    request.session['items_ordered'] = request.session['items_ordered'] + int(request.POST['quantity'])

    if word == 'tshirt':
        price = 19.99
    elif word == 'sweater':
        price = 29.99
    elif word == 'cup':
        price = 4.99
    elif word == 'book':
        price = 49.99

    request.session['this_price'] = price * int(request.POST['quantity'])

    request.session['cash_spent'] = request.session['cash_spent'] + request.session['this_price']

    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')
