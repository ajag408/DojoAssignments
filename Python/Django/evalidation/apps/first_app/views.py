from django.shortcuts import render, redirect
from .models import User, UserManager

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def validate(request):
    # User.objects.create(email=request.POST['email'])
    check = User.objects.validate(request.POST['email'])
    if check is True:
        message = "Email is valid"
        context = {
            'message': message,
            'emails': User.objects.all()
        }
        return render(request, 'first_app/success.html', context)
    else:
        message = "email "+ request.POST['email'] + " is invalid"
        context = {
            'message': message
        }

        return render(request, 'first_app/home.html', context)

def delete(request, id):
    User.objects.get(id=id).delete()
    context = {
        'emails': User.objects.all()
    }
    return render(request, 'first_app/success.html', context)
