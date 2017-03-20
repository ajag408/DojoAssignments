from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def timedisplay(request):
    context = {
        'current_time': datetime.datetime.now()
    }
    return render(request, 'timedisplay/index.html', context)
