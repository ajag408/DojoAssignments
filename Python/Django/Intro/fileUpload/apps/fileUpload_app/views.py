from django.shortcuts import render, redirect
from django import forms


# Create your views here.
def handle_uploaded_file(f):
    with open('./apps/fileUpload_app/uploads', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    return render(request, 'fileUpload_app/index.html')

def upload(request):
    if 'file' in request.FILES:
        handle_uploaded_file(request.FILES['file'])

    return redirect('/')
