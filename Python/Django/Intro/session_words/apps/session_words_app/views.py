from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import pytz

# Create your views here.
def index(request):
    if 'word_list' not in request.session:
        request.session['word_list'] = []
    return render(request, 'session_words_app/index.html')

def add_word(request):
    word = request.POST['word']
    color = request.POST['color']
    if 'bigFont' in request.POST:
        font = 'big'
    else:
        font = 'small'
    date_format = "%I:%M:%S%p, %B %dth %Y"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    added_on = "added on " + date.strftime(date_format)
    new_word = {'word': word, 'color': color, 'font': font, 'added_on': added_on}
    request.session['word_list'].append(new_word)
    request.session['word_list'] = request.session['word_list']
    return redirect('/')

def clear_session(request):
    if 'word_list' in request.session:
        del request.session['word_list']
    return redirect('/')
