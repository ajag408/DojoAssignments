from django.shortcuts import render, redirect
from models import *

# Create your views here.
def render_users(request):
    return redirect('/users')

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users_app/index.html', context)

def new(request):
    return render(request, 'users_app/new.html')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, 'users_app/edit.html', context)

def show(request, user_id):
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

    context = {
        'user': user
    }
    return render(request, 'users_app/show.html', context)


def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    User.objects.create(first_name = first_name, last_name = last_name, email = email)
    return redirect('/users')

def destroy(request, user_id):
    done_for = User.objects.get(id = user_id)
    done_for.delete()
    return redirect('/users')
