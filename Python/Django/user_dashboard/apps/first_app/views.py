from django.shortcuts import render, redirect
from .models import User, UserManager, Admin
import bcrypt
# Create your views here.
def home(request):

    return render(request, 'first_app/home.html')

def render_signin(request):
    return render(request, 'first_app/signin.html')

def render_register(request):
    return render(request, 'first_app/register.html')

def validate_register(request):
    check1 = User.objects.check_first_name(request.POST['first_name'])
    if check1 is False:
        error1 = "First name: required; no fewer than 2 characters; letters only"
        context = {
            'error1': error1
        }
        return render(request, 'first_app/register.html', context)
    check2 = User.objects.check_last_name(request.POST['last_name'])
    if check2 is False:
        error2 = "Last name: required; no fewer than 2 characters; letters only"
        context = {
            'error2': error2
        }
        return render(request, 'first_app/register.html', context)
    check3 = User.objects.check_email(request.POST['email'])
    if check3 is False:
        error3 = "Email: Required; Valid Format"
        context = {
            'error3': error3
        }
        return render(request, 'first_app/register.html', context)
    check4 = User.objects.check_password_1(request.POST['password'])
    if check4 is False:
        error4 = "Password: Required; No fewer than 8 characters in length"
        context = {
            'error4': error4
        }
        return render(request, 'first_app/register.html', context)
    check5 = User.objects.check_password_2(request.POST['password'], request.POST['pconf'])
    if check5 is False:
        error5 = "Password must match password confirmation"
        context = {
            'error5': error5
        }
        return render(request, 'first_app/register.html', context)

    register = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['pconf'])
    if register is False:
        error7 = "User already exists!"
        context = {
            'error7': error7
        }
        return render(request, 'first_app/register.html', context)
    if register is True:
        first_one=Admin.objects.filter(user_id__email = request.POST['email'])
        if first_one.exists():
            context = {
                'this_user': User.objects.get(email = request.POST['email']),
                'users': User.objects.all(),
                'admins': Admin.objects.all()
            }
            return render(request, 'first_app/admin_dashboard.html', context)
        else:
            context = {
                'this_user': User.objects.get(email = request.POST['email']),
                'users': User.objects.all(),
                'admins': Admin.objects.all()
            }
            return render(request, 'first_app/user_dashboard.html', context)

def login(request):
    login = User.objects.login(request.POST['email'],request.POST['password'])
    if login is True:
        admins = Admin.objects.all()
        for admin in admins:
            if admin.user_id.email == request.POST['email']:
                context = {
                    'this_user': User.objects.get(email = request.POST['email']),
                    'users': User.objects.all(),
                    'admins': Admin.objects.all()
                }
                return render(request, 'first_app/admin_dashboard.html', context)
        context = {
                'this_user': User.objects.get(email = request.POST['email']),
                'users': User.objects.all(),
                'admins': Admin.objects.all()
            }
        return render(request, 'first_app/user_dashboard.html', context)
    else:
        error6 = "Log-in failed: check email and password"
        context = {
            'error6': error6
        }
        return render(request, 'first_app/signin.html', context)

def logout(request):
    return render(request, 'first_app/home.html')

def render_dashboard(request,id):
    admins = Admin.objects.all()
    for admin in admins:
        if admin.user_id.id == int(id):
            context = {
                'this_user': User.objects.get(id = id),
                'users': User.objects.all(),
                'admins': Admin.objects.all()
            }
            return render(request, 'first_app/admin_dashboard.html', context)
    context = {
        'this_user': User.objects.get(id = id),
        'users': User.objects.all(),
        'admins': Admin.objects.all()
    }
    return render(request, 'first_app/user_dashboard.html', context)

def render_add_new(request,id):
    context = {
        'this_user': User.objects.get(id=id)
    }
    return render(request,'first_app/add_new.html', context)

def add_new(request,id):
    register = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['pconf'])
    if register is False:
        context = {
            'this_user': User.objects.get(id=id)
        }
        return render(request, 'first_app/add_new.html', context)
    if register is True:
        context = {
            'this_user': User.objects.get(id = id),
            'users': User.objects.all(),
            'admins': Admin.objects.all()
        }
        return render(request, 'first_app/admin_dashboard.html', context)

def render_edit_profile(request,id):
    context = {
        'this_user': User.objects.get(id=id)
    }
    return render(request, 'first_app/edit_profile.html', context)

def render_edit_user(request,user_id,admin_id):
    context={
        'user': User.objects.get(id=user_id),
        'admin': User.objects.get(id=admin_id)
    }
    return render(request, 'first_app/edit_user.html', context)

def edit_info(request,id):
    user = User.objects.get(id=id)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()

    context = {
        'this_user': User.objects.get(id = id),
        }

    return render(request, 'first_app/edit_profile.html', context)

def admin_edit_info(request,user_id, admin_id):
    user = User.objects.get(id= user_id)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    if request.POST['user_level'] == 'admin':
        Admin.objects.create(user_id = User.objects.get(id=user_id))
    user.save()

    context = {
        'user': User.objects.get(id= user_id),
        'admin': User.objects.get(id = admin_id)
        }

    return render(request, 'first_app/edit_user.html', context)

def admin_change_pw(request,user_id,admin_id):
    user = User.objects.get(id=id)
    password = request.POST['password']
    password = password.encode()
    pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    user.pw_hash = pw_hash
    user.save()

    context={
        'user': User.objects.get(id=user_id),
        'admin': User.objects.get(id = admin_id)
    }

    return render(request, 'first_app/edit_user.html', context)


def change_pw(request,id):
    user = User.objects.get(id=id)
    password = request.POST['password']
    password = password.encode()
    pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    user.pw_hash = pw_hash
    user.save()

    context={
        'this_user': User.objects.get(id = id),
    }

    return render(request, 'first_app/edit_profile.html', context)

def edit_description(request,id):
    user = User.objects.get(id=id)
    user.description = request.POST['description']
    user.save()

    context={
        'this_user': User.objects.get(id = id),
    }

    return render(request, 'first_app/edit_profile.html', context)

def render_user_page(request,user_id,admin_id):
    context={
        'user_wall': User.objects.get(id=user_id),
        'this_user': User.objects.get(id=admin_id),
        'messages': Message.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request, 'first_app/user_page.html', context)

def post_message(request, user_wall_id, this_user_id):
    Message.objects.create(postman_id = User.objects.get(id = this_user_id ), wall_id = User.objects.get(id = user_wall_id), message = request.POST['message'])
    context = {
        'user_wall': User.objects.get(id=user_wall_id),
        'this_user': User.objects.get(id=this_user_id),
        'messages': Message.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request, 'first_app/user_page.html', context)

def post_comment(request, message_id, user_wall_id, this_user_id):
    Comment.objects.create(message_id = Message.objects.get(id = message_id), commenter_id = User.objects.get(id = this_user_id), comment= request.POST['comment'])
    context={
        'user_wall': User.objects.get(id = user_wall_id),
        'this_user': User.objects.get(id=this_user_id),
        'messages': Message.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request, 'first_app/user_page.html', context)
