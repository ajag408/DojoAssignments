from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('/login_reg/')

def test_api(request):
    return render(request, 'pokeApp/index.html')
