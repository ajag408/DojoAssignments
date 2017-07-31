from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.core import serializers
# the index function is called when root is visited
def index(request):
    return render(request, 'orm_app/index.html')

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize('json', users)
    return HttpResponse(users_json, content_type = 'application/json')

def all_html(request):
    users = User.objects.all()
    return render(request, 'orm_app/all.html', {'users': users})
