from django.shortcuts import render, HttpResponse
from datetime import datetime
from pytz import timezone
import pytz

# Create your views here.
def timedisplay(request):
    date_format="%Y-%m-%d %H:%M %p"
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    current_time = date.strftime(date_format)

    context = {
        'current_time': current_time
    }
    return render(request, 'timedisplay/index.html', context)
