from django.shortcuts import render, redirect
from models import *
# Create your views here.
def index(request):
    notes = Post.objects.all()
    return render(request, 'ajax_post/index.html', {'notes': notes})

def add_post(request):
    Post.objects.create(note = request.POST['note'])
    this_post = Post.objects.last()
    this_post = this_post.note

    return render(request, 'ajax_post/fresh_post.html', {'this_post': this_post})
