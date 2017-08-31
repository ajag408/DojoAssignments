from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager
from django.contrib import messages
import requests
# Create your views here.
def home(request):
    r = requests.get('http:/www.pokeapi.co/media/img/1.png')
    print type(r)
    return render(request, 'first_app/home.html')

def validate_register(request):
    check1 = User.objects.check_first_name(request.POST['first_name'])
    if check1 is False:
        messages.error(request,"First name: required; no fewer than 2 characters; letters only")
        return redirect('/login_reg/')

    check2 = User.objects.check_last_name(request.POST['last_name'])
    if check2 is False:
        messages.error(request,"Last name: required; no fewer than 2 characters; letters only")
        return redirect('/login_reg/')

    check3 = User.objects.check_email(request.POST['email'])
    if check3 is False:
        messages.error(request,"Email: Required; Valid Format")
        return redirect('/login_reg/')

    check4 = User.objects.check_birthday(request.POST['birthday'])
    if check4 is False:
        messages.error(request,'birthday must be valid')
        return redirect('/login_reg/')

    check5 = User.objects.check_password_1(request.POST['password'])
    if check5 is False:
        messages.error(request,"Password: Required; No fewer than 8 characters in length")
        return redirect('/login_reg/')

    check6 = User.objects.check_password_2(request.POST['password'], request.POST['pconf'])
    if check5 is False:
        messages.error(request,"Password must match password confirmation")
        return redirect('/login_reg/')


    register = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'], request.POST['birthday'], request.POST['password'],request.POST['pconf'])
    if register is False:
        messages.error(request,"User already exists!")
        return redirect('/login_reg/')

    if register is True:
        this_user = User.objects.get(email = request.POST['email'])
        request.session['user'] = this_user.id
        return redirect('/login_reg/success')

def success(request):
    this_user = User.objects.get(id = request.session['user'])
    context = {
        'user': this_user
    }

    return render(request, 'first_app/success.html', context)

def login(request):
    login = User.objects.login(request.POST['email'],request.POST['password'])
    if login is True:
        this_user = User.objects.get(email = request.POST['email'])
        request.session['user'] = this_user.id
        return redirect('/login_reg/success')
    else:
        messages.error(request, "Log-in failed: check email and password")
        return redirect('/login_reg/')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/login_reg/')

def render_field(request):
    return render(request, 'first_app/field.html')

def collect(request):
    print request.POST
    return HttpResponse('safe')
