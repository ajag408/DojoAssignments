from django.shortcuts import render, redirect
from .models import User, UserManager, Trip, TripManager
from datetime import datetime

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
            'this_user': User.objects.get(email = request.POST['email']),
            'other_users': User.objects.all().exclude(email = request.POST['email']),
            'other_user_trips': Trip.objects.all().exclude(pilgrims__email = request.POST['email'])
        }
        return render(request, 'first_app/travel_dashboard.html', context)

def login(request):
    login = User.objects.login(request.POST['email'],request.POST['password'])


    if login is True:
        # trip1 = Trip.objects.filter(id = 2)
        # user1 = User.objects.get(email = request.POST['email'])
        # for trips in trip1:
        #     trips.pilgrims.add(user1)
        #
        # print Trip.objects.all().values('pilgrims')

        # this_user_test = User.objects.get(email = request.POST['email'])
        # for user in User.objects.all().exclude(email = request.POST['email']):
        #     for trip in user.made_trip.all():
        #         if this_user_test not in trip.pilgrims.all():
        #             print trip.destination
        message = "Successfully logged-in"
        context = {
            'message':message,
            'this_user': User.objects.get(email = request.POST['email']),
            'user_trips': Trip.objects.filter(pilgrims__email = request.POST['email']),
            'other_users': User.objects.all().exclude(email = request.POST['email']),
            # 'other_user_trips': other_user_trips
            }



        return render(request, 'first_app/travel_dashboard.html', context)
    else:
        error6 = "Log-in failed: check email and password"
        context = {
            'error6': error6
        }
        return render(request, 'first_app/home.html', context)

def logout(request):
    return render(request, 'first_app/home.html')

def home_render(request,id):
    context = {

        'this_user': User.objects.get(id = id),
        'user_trips': Trip.objects.filter(pilgrims__id = id),
        'other_users': User.objects.all().exclude(id = id),
        # 'other_user_trips': Trip.objects.all().exclude(pilgrims__id = id)
        }
    return render(request, 'first_app/travel_dashboard.html', context)


def travel_plan_page(request, id):
    context = {
        'this_user': User.objects.get(id = id)
    }
    return render(request, 'first_app/add_plan.html', context)

def add_plan(request, id):
    # start =datetime.strptime(request.POST['start_date'], '%Y-%m-%d')
    # end = datetime.strptime(request.POST['end_date'], '%Y-%m-%d')
    # if start > end:
    #     print 0
    # else:
    #     print 1
    # print datetime.now()
    valid_trip = Trip.objects.validate_trip(request.POST['destination'], request.POST['description'], request.POST['start_date'], request.POST['end_date'])
    if valid_trip is True:
        new_trip = Trip.objects.create(destination = request.POST['destination'], description = request.POST['description'], start_date = request.POST['start_date'], end_date = request.POST['end_date'], user_creator_id = User.objects.get(id = id))
        new_trip_iterable = Trip.objects.filter(user_creator_id = User.objects.get(id = id))
        for trip in new_trip_iterable:
            trip.pilgrims.add(User.objects.get(id=id))
        context = {
            'this_user': User.objects.get(id=id),
            'user_trips': Trip.objects.filter(pilgrims__id=id),
            'other_users': User.objects.all().exclude(id = id),
            # 'other_user_trips': Trip.objects.all().exclude(pilgrims__id = id)
        }
        return render(request, 'first_app/travel_dashboard.html', context)
    else:
        print False
        message = "Make sure all inputs are valid (no empty entries, travel dates future-added, starts before it ends)"
        context = {
            'message': message,
            'user': User.objects.get(id=id)
        }
        return render(request, 'first_app/add_plan.html', context)

def destination_page(request, id):
    context = {
        'this_user': User.objects.get(id=id),
        'this_trip': Trip.objects.get(id = request.POST['trip']),
        'trip_creator': User.objects.get(made_trip__id = request.POST['trip']),
        'pilgrims': User.objects.filter(trips__id = request.POST['trip'])
    }

    return render(request, 'first_app/destination.html', context)

def join(request,id):
            # trip1 = Trip.objects.filter(id = 2)
            # user1 = User.objects.get(email = request.POST['email'])
            # for trips in trip1:
            #     trips.pilgrims.add(user1)
    this_trip = Trip.objects.filter(id = request.POST['trip'])
    user = User.objects.get(id=id)
    for trip in this_trip:
        trip.pilgrims.add(user)




    context = {
        'this_user': User.objects.get(id=id),
        'user_trips': Trip.objects.filter(pilgrims__id=id),
        'other_users': User.objects.all().exclude(id = id),
        # 'other_user_trips': Trip.objects.all().exclude(pilgrims__id = id)
    }
    return render(request,'first_app/travel_dashboard.html', context)
