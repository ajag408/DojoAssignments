from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
    return redirect('/users')

def users_home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users_app/index.html', context)

def render_add_user(request):
    return render(request, 'users_app/new.html')
