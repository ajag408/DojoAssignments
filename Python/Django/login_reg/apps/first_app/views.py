from django.shortcuts import render, redirect
from .models import User, UserManager
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def validate_register(request):
    check1 = User.objects.check_first_name(request.POST['first_name'])
    if check1 is False:
        error1 = "First name: required; no fewer than 2 characters; letters only"
        context = {
            'error1': error1
        }
        return render(request, 'first_app/home.html', context)
    check2 = User.objects.check_last_name(request.POST['last_name'])
    if check2 is False:
        error2 = "Last name: required; no fewer than 2 characters; letters only"
        context = {
            'error2': error2
        }
        return render(request, 'first_app/home.html', context)
    check3 = User.objects.check_email(request.POST['email'])
    if check3 is False:
        error3 = "Email: Required; Valid Format"
        context = {
            'error3': error3
        }
        return render(request, 'first_app/home.html', context)
    check4 = User.objects.check_password_1(request.POST['password'])
    if check4 is False:
        error4 = "Password: Required; No fewer than 8 characters in length"
        context = {
            'error4': error4
        }
        return render(request, 'first_app/home.html', context)
    check5 = User.objects.check_password_2(request.POST['password'], request.POST['pconf'])
    if check5 is False:
        error5 = "Password must match password confirmation"
        context = {
            'error5': error5
        }
        return render(request, 'first_app/home.html', context)

    register = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['pconf'])
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
        error6 = "Log-in failed: check email and password"
        context = {
            'error6': error6
        }
        return render(request, 'first_app/home.html', context)

def logout(request):
    return render(request, 'first_app/home.html')
