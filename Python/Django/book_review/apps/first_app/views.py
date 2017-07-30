from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def validate_register(request):
    check1 = User.objects.check_first_name(request.POST['first_name'])
    if check1 is False:
        messages.error(request, "First name: required; no fewer than 2 characters; letters only")
        return redirect('/')

    check2 = User.objects.check_last_name(request.POST['last_name'])
    if check2 is False:
        messages.error(request, "Last name: required; no fewer than 2 characters; letters only")
        return redirect('/')

    check3 = User.objects.check_email_1(request.POST['email'])
    if check3 is False:
        messages.error(request, "Email: Required; Valid Format")
        return redirect('/')

    check6 = User.objects.check_email_2(request.POST['email'])
    if check6 is False:
        messages.error(request, 'email is already taken')
        return redirect('/')

    check4 = User.objects.check_password_1(request.POST['password'])
    if check4 is False:
        messages.error(request, "Password: Required; No fewer than 8 characters in length")
        return redirect('/')

    check5 = User.objects.check_password_2(request.POST['password'], request.POST['pconf'])
    if check5 is False:
        messages.error(request, "Password must match password confirmation")
        return redirect('/')

    register = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['pconf'])
    if register is False:
        messages.error(request, "User already exists!")
        return redirect('/')

    if register is True:
        this_user = User.objects.get(email = request.POST['email'])
        request.session['user'] = this_user.id
        return redirect('/review_home')

def login(request):
    login = User.objects.login(request.POST['email'],request.POST['password'])
    if login is True:
        review_count = Review.objects.count()
        review1 = Review.objects.get(id = review_count)
        review2 = Review.objects.get(id = review_count -1)
        review3 = Review.objects.get(id = review_count -2)

        i = 1
        other_reviews = []
        while i<(review_count-2):
            other_reviews.append(Review.objects.filter(id = i))
            i = i + 1
        print other_reviews
        context = {

            'user': User.objects.get(email = request.POST['email']),
            'review1': review1,
            'review2': review2,
            'review3': review3,
            'other_reviews': other_reviews
            }

        return render(request, 'first_app/success.html', context)
    else:
        error6 = "Log-in failed: check email and password"
        context = {
            'error6': error6
        }
        return render(request, 'first_app/home.html', context)

def review_home(request):
    review_count = Review.objects.count()
    review1 = Review.objects.get(id = review_count)
    review2 = Review.objects.get(id = review_count -1)
    review3 = Review.objects.get(id = review_count -2)

    i = 1
    other_reviews = []
    while i<(review_count-2):
        other_reviews.append(Review.objects.filter(id = i))
        i = i + 1

    context = {

        'user': User.objects.get(id = request.session['user']),
        'review1': review1,
        'review2': review2,
        'review3': review3,
        'other_reviews': other_reviews
        }

    return render(request, 'first_app/success.html', context)

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')

def new_two(request):
    context = {
        'user': User.objects.get(id=request.session['user']),
        'books': Book.objects.all()
    }
    return render(request,'first_app/new_two.html', context)

def render_book_page(request, book_render_id):
        context = {
            'user': User.objects.get(id= request.session['user']),
            'book': Book.objects.get(id = book_render_id),
            'reviews': Review.objects.filter(book_id = Book.objects.get(id = book_render_id))
            }
        return render(request,'first_app/book_page.html', context)

def render_user_page(request, user_render_id):
    user_reviews = Review.objects.filter(user_id = user_render_id)
    review_count = Review.objects.filter(user_id = user_render_id).count()
    context = {
    'user': User.objects.get(id= request.session['user']),
    'rendered_user': User.objects.get(id = user_render_id),
    'review_count': review_count,
    'user_reviews': user_reviews
    }
    return render(request, 'first_app/user_page.html', context)

def add_book(request):
    checker = 'my_hoffa'
    if checker in request.POST:
        Book.objects.create(title = request.POST['title'], author = request.POST['my_hoffa'])
    else:
        Book.objects.create(title = request.POST['title'], author = request.POST['author'])

    Review.objects.create(book_id = Book.objects.get(title = request.POST['title']), user_id = User.objects.get(id=request.session['user']), rating = int(request.POST['rating']), content = request.POST['review'])
    this_book = Book.objects.get(title = request.POST['title'])
    book_render_id = this_book.id
    return redirect('/render_book_page/'+str(book_render_id))

def add_review(request, this_book_id):
    Review.objects.create(book_id = Book.objects.get(id = this_book_id), user_id = User.objects.get(id=request.session['user']), rating = int(request.POST['rating']), content = request.POST['review'])

    return redirect('/render_book_page/'+str(this_book_id))
