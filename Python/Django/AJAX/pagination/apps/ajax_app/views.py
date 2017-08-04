from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from models import *
from datetime import datetime
import pytz
# Create your views here.
@ensure_csrf_cookie
def index(request):
    leads = Lead.objects.filter(page = 1)
    return render(request, 'ajax_app/index.html', {'leads': leads})

def index2(request):
    leads = Lead.objects.filter(page =2)
    return render(request, 'ajax_app/index2.html', {'leads':leads})

def index3(request):
    leads = Lead.objects.filter(page=3)
    return render(request, 'ajax_app/index3.html', {'leads': leads})

def add_lead(request):
    complete = Lead.objects.isValid(request.POST)
    if complete is True:
        Lead.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], page = int(request.POST['page']))
        lead = Lead.objects.last()
        return render(request, 'ajax_app/fresh_lead.html', {'lead': lead})
    else:
        return render(request, 'ajax_app/fresh_lead.html')


def edit_lead(request, lead_id):
    this_lead = Lead.objects.get(id = lead_id)
    this_lead.first_name = request.POST['first_name']
    this_lead.last_name = request.POST['last_name']
    this_lead.email = request.POST['email']
    this_lead.save()
    return HttpResponse('lead saved')

def filter(request, page):
    dateFrom = request.POST['from']
    dateFrom = datetime.strptime(dateFrom, '%Y-%m-%d')
    dateFrom = pytz.utc.localize(dateFrom)

    dateTo = request.POST['to']
    dateTo = datetime.strptime(dateTo, '%Y-%m-%d')
    dateTo = pytz.utc.localize(dateTo)

    leads = Lead.objects.filter(page = page, first_name__startswith=request.POST['first_name'], registered_datetime__gt = dateFrom, registered_datetime__lt = dateTo)
    return render(request, 'ajax_app/all.html', {'leads': leads})
