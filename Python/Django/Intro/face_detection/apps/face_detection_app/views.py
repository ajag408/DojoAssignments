from django.shortcuts import render, redirect
from django import forms
import os


# Create your views here.
def handle_uploaded_file(f):
    with open('./apps/face_detection_app/upload.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    return render(request, 'face_detection_app/index.html')

def upload(request):
    if 'file' in request.FILES:
        handle_uploaded_file(request.FILES['file'])
        os.system('python ./apps/face_detection_app/face_detect_cv3.py ./apps/face_detection_app/upload.png ./apps/face_detection_app/haarcascade_frontalface_default.xml')

    return redirect('/')
