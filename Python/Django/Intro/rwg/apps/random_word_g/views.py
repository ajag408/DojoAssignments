from django.shortcuts import render, redirect
import random, string

# Create your views here.
def index(request):
    if 'word' not in request.session:
        request.session['word'] = ''.join(random.sample(string.ascii_lowercase, 14))
    if 'count' not in request.session:
        request.session['count'] = 1

    return render(request, 'random_word_g/index.html')

def randomstr(request):
    if request.method =='POST':
        request.session['word'] = ''.join(random.sample(string.ascii_lowercase, 14))
        request.session['count'] = int(request.session['count']) + 1

        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    if 'count' in request.session:
        del request.session['count']

    return redirect('/')
