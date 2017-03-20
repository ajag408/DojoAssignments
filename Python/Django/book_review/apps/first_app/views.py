from django.shortcuts import render, redirect
from .models import User, UserManager, Book, Review
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
            'user': User.objects.get(email = request.POST['email']),
            'review1': review1,
            'review2': review2,
            'review3': review3,
            'other_reviews': other_reviews
        }
        return render(request, 'first_app/success.html', context)

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

def review_home(request, id):
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

        'user': User.objects.get(id = id),
        'review1': review1,
        'review2': review2,
        'review3': review3,
        'other_reviews': other_reviews
        }

    return render(request, 'first_app/success.html', context)
    
def logout(request):
    return render(request, 'first_app/home.html')

def new_two(request,id):
    context = {
        'user': User.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request,'first_app/new_two.html', context)

def render_book_page(request, book_render_id, user_id):
        context = {
            'user': User.objects.get(id= user_id),
            'book': Book.objects.get(id = book_render_id),
            'reviews': Review.objects.filter(book_id = Book.objects.get(id = book_render_id))
            }
        return render(request,'first_app/book_page.html', context)

def render_user_page(request, user_render_id, id):
    user_reviews = Review.objects.filter(user_id = user_render_id)
    review_count = Review.objects.filter(user_id = user_render_id).count()
    context = {
    'user': User.objects.get(id= id),
    'rendered_user': User.objects.get(id = user_render_id),
    'review_count': review_count,
    'user_reviews': user_reviews
    }
    return render(request, 'first_app/user_page.html', context)

def add_book(request, id):
    checker = 'my_hoffa'
    if checker in request.POST:
        Book.objects.create(title = request.POST['title'], author = request.POST['my_hoffa'])
    else:
        Book.objects.create(title = request.POST['title'], author = request.POST['author'])

    Review.objects.create(book_id = Book.objects.get(title = request.POST['title']), user_id = User.objects.get(id=id), rating = int(request.POST['rating']), content = request.POST['review'])
    this_book = Book.objects.get(title = request.POST['title'])
    book_render_id = this_book.id
    return redirect('/render_book_page/'+str(book_render_id)+'/'+str(id))

def add_review(request, this_book_id, user_id):
    Review.objects.create(book_id = Book.objects.get(id = this_book_id), user_id = User.objects.get(id=user_id), rating = int(request.POST['rating']), content = request.POST['review'])

    return redirect('/render_book_page/'+str(this_book_id)+'/'+str(user_id))
