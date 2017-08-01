from django.shortcuts import render, HttpResponse
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    notes = Note.objects.all()
    return render(request, 'notes_app/index.html', {'notes': notes})

def add_note(request):
    isValid = Note.objects.isValid(request.POST)
    if isValid is False:
        messages.error(request, "Please enter something")
    else:
        Note.objects.create(title = request.POST['title'], description = '')
        messages.success(request, 'Note added')
    notes = Note.objects.all()
    return render(request, 'notes_app/fresh_note.html', {'notes': notes})

def add_description(request, note_id):
    note = Note.objects.get(id = note_id)
    note.description = request.POST['description']
    note.save()
    return HttpResponse('description saved')

def delete(request, note_id):
    Note.objects.get(id = note_id).delete()
    notes = Note.objects.all()
    return render(request, 'notes_app/fresh_note.html', {'notes': notes})
