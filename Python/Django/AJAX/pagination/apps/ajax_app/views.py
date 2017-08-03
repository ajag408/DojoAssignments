from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from models import *
# Create your views here.
@ensure_csrf_cookie
def index(request):
    leads = Lead.objects.all()
    return render(request, 'ajax_app/index.html', {'leads': leads})


def add_lead(request):
    complete = Lead.objects.isValid(request.POST)
    if complete is True:
        Lead.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        lead = Lead.objects.last()
        return render(request, 'ajax_app/fresh_lead.html', {'lead': lead})
    else:
        return render(request, 'ajax_app/fresh_lead.html')


def edit_lead(request, lead_id):
    this_lead = Lead.objects.get(id = lead_id)
    this_lead.first_name = request.POST['first_name']
    this_lead.last_name = request.POST['last_name']
    this_lead.email = request.POST['email']
    print this_lead.email
    this_lead.save()
    print this_lead.email
    return HttpResponse('lead saved')
