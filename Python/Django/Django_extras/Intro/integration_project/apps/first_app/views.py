from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def validate_register(request):
    check1 = User.objects.check_first_name(request.POST['first_name'])
    if check1 is False:
        messages.error(request,"First name: required; no fewer than 2 characters; letters only")
        return render(request, 'first_app/home.html')

    check2 = User.objects.check_last_name(request.POST['last_name'])
    if check2 is False:
        messages.error(request,"Last name: required; no fewer than 2 characters; letters only")
        return render(request, 'first_app/home.html')

    check3 = User.objects.check_email(request.POST['email'])
    if check3 is False:
        error3 = "Email: Required; Valid Format"
        context = {
            'error3': error3
        }
        return render(request, 'first_app/home.html', context)

    check4 = User.objects.check_birthday(request.POST['birthday'])
    if check4 is False:
        error4 = 'birthday must be valid'
        context = {
            'error4': error4
        }
        return render(request, 'first_app/home.html', context)

    check5 = User.objects.check_password_1(request.POST['password'])
    if check5 is False:
        error5 = "Password: Required; No fewer than 8 characters in length"
        context = {
            'error5': error5
        }
        return render(request, 'first_app/home.html', context)
    check6 = User.objects.check_password_2(request.POST['password'], request.POST['pconf'])
    if check5 is False:
        error6 = "Password must match password confirmation"
        context = {
            'error6': error6
        }
        return render(request, 'first_app/home.html', context)

    print request.POST['birthday']

    register = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'], request.POST['birthday'], request.POST['password'],request.POST['pconf'])
    if register is False:
        error7 = "User already exists!"
        context = {
            'error7': error7
        }
        return render(request, 'first_app/home.html', context)
    if register is True:
        message = "Successfully registered and logged-in"
        context = {
            'message': message,
            'user': User.objects.get(email = request.POST['email'])
        }
        return render(request, 'first_app/success.html', context)

def login(request):
    login = User.objects.login(request.POST['email'],request.POST['password'])
    if login is True:
        message = "Successfully logged-in"
        context = {
            'message':message,
            'user': User.objects.get(email = request.POST['email'])
            }

        return render(request, 'first_app/success.html', context)
    else:
        error8 = "Log-in failed: check email and password"
        context = {
            'error8': error8
        }
        return render(request, 'first_app/home.html', context)

def logout(request):
    return render(request, 'first_app/home.html')
