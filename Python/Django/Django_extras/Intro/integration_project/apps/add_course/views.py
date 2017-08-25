from django.shortcuts import render, redirect
from models import *
# Create your views here.
def home(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'add_course/home.html', context)

def users_courses(request):
    courses = Course.objects.all()
    for course in courses:
        course.user_count = 0
        for user in course.users.all():
            course.user_count = course.user_count + 1
        course.save()
    context = {
        'courses': courses,
        'users': User.objects.all()
    }

    return render(request, 'add_course/users_courses.html', context)

def add_user_course(request):
    course = Course.objects.get(name = request.POST['course'])
    user = User.objects.get(first_name = request.POST['user'])

    course.users.add(user)

    course.save()

    return redirect('/courses/users_courses')



def add(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        return redirect('/courses/')
    else:
        this_course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(course = this_course, description=request.POST['description'])
        return redirect('/courses/')

def renderDelete(request, id):
    this_course = Course.objects.get(id=id)
    description = Description.objects.get(course = this_course)
    context = {
        'this_course': this_course,
        'description': description
    }

    return render(request, 'add_course/delete.html', context)

def delete(request, id):
    this_course = Course.objects.get(id=id)
    description = Description.objects.get(course = this_course)
    this_course.delete()
    description.delete()
    return redirect('/')

def comments(request,id):
    this_course = Course.objects.get(id = id)
    print this_course.comments.all()
    context = {
        'this_course': Course.objects.get(id = id)
    }

    return render(request, 'add_course/comments.html', context)

def add_comment(request,id):
    Comment.objects.create(course = Course.objects.get(id=id), comment = request.POST['comment'])
    return redirect('/comments/' + str(id))
