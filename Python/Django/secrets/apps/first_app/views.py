from django.shortcuts import render, redirect
from .models import User, UserManager, Secret, SecretManager, Like
from django.db.models import Count
import datetime, collections
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
        this_id = User.objects.get(email = request.POST['email']).value('id').annotate(Count('id'))
        this_id_val = this_id[0]['id']
        print this_id_val
        return redirect('/secrets.html' + str(this_id_val))

def secret_home(request, id):
    secret_display = []
    secret_count = Secret.objects.count()
    secret_saver = []
    secret_index = []


    start_secret = Secret.objects.all().values('id').annotate(Count('id'))
    start = start_secret[len(start_secret)-1]['id']
    for i in range(start):
        while len(secret_index)<10:

            c1 = Secret.objects.filter(id = start - i).values('created_at').annotate(Count('created_at'))
            if c1.exists():
                if i < start:
                    c1 = Secret.objects.filter(id = start - i).values('created_at').annotate(Count('created_at'))
                    time_elapsed = int(datetime.datetime.now().strftime('%M')) - int(c1[0]['created_at'].strftime('%M'))
                    secret_to_append = Secret.objects.filter(id = start - i).values('content').annotate(Count('content'))
                    secret_saver.append(Secret.objects.filter(id = start-i))
                    secret_likes = Like.objects.filter(worthySecret = Secret.objects.get(id=start- i)).count()
                    secret_display.append(secret_to_append[0]['content'] + " (" + str(time_elapsed) + " minutes ago) " + str(secret_likes) + " likes")
                    secret_index.append(start - i)

                    i = i + 1
                else:
                    i = i + 1
            else:
                i = i+1




    posted = []
    liked = []
    post_bool = {}
    like_bool = {}
    steez_list = []
    keyz_list = []

    for x in range(start,0,-1):
        secret_in_question = Secret.objects.filter(id = x)
        if secret_in_question.exists():
            secret_check1 = Secret.objects.filter(id = x).values('secret_maker').annotate(Count('secret_maker'))
            secret_check2 = User.objects.filter(id=id).values('id').annotate(Count('id'))
            if secret_check1[0]['secret_maker'] == secret_check2[0]['id']:

                posted = []
                poster = "You posted this"
                posted.append(poster)
                post_bool[x] = True

    for y in range(start, 0, -1):
        s1 = Secret.objects.filter(id = y)
        if s1.exists():
            liker_check1 = Like.objects.filter(worthySecret = Secret.objects.get(id = y)).values('liker').annotate(Count('liker'))
            liker_check2 = User.objects.filter(id=id).values('id').annotate(Count('id'))
            if liker_check1.exists():
                for i, c in enumerate(liker_check1):
                    if c['liker'] == liker_check2[0]['id']:
                        liked = []
                        likey = 'you liked this'
                        liked.append(likey)
                        like_bool[y] = True

    for steez in post_bool:
        steez_list.append(steez)

    for keyz in like_bool:
        keyz_list.append(keyz)





    secret_maachan = zip(secret_index, secret_display)
    secret_maachan_dict = dict(secret_maachan)
    od = collections.OrderedDict(reversed(sorted(secret_maachan_dict.items())))


    context = {
                'user': User.objects.get(id = id),
                'secret_maachan': od,
                'poster2': posted,
                'likey2': liked,
                'post_bool': post_bool,
                'like_bool': like_bool,
                'keyz_list': keyz_list,
                'steez_list': steez_list


                }

    return render(request,'first_app/secrets.html', context)

def login(request):
    login = User.objects.login(request.POST['email'],request.POST['password'])
    if login is True:

        user_id_raw = User.objects.filter(email = request.POST['email']).values('id').annotate(Count('id'))
        user_id = user_id_raw[0]['id']
        return redirect('/secret_home/'+str(user_id))
    else:
        error6 = "Log-in failed: check email and password"
        context = {
            'error6': error6
        }
        return render(request, 'first_app/home.html', context)



def logout(request):
    return render(request, 'first_app/home.html')

def create_secret(request, id):
    Secret.objects.push_to_database(content = request.POST['secret'], this_user = id)
    return redirect('/secret_home/' + str(id))

def like(request, id):
    new_like = Like.objects.create(worthySecret=Secret.objects.get(id = request.POST['secret_index']))
    new_like.liker.add(User.objects.get(id = id))
    return redirect('/secret_home/' +str(id))

def like2(request,id):
    new_like = Like.objects.create(worthySecret=Secret.objects.get(id=request.POST['secret_index']))
    new_like.liker.add(User.objects.get(id=id))
    return redirect('/popular/' +str(id))

def delete1(request,id):
    Secret.objects.filter(id = request.POST['secret_index']).delete()
    return redirect('/secret_home/' +str(id))

def delete2(request,id):
    Secret.objects.filter(id=request.POST['secret_index']).delete()
    return redirect('/popular/' +str(id))

def popular(request, id):
    secret_content_ordered = []
    secret_likes_ordered = []
    ordered_pop = Secret.objects.all().annotate(like_index = Count('likes')).order_by('-like_index')

    for i in ordered_pop:
        secret_content_ordered.append(i)
        secret_likes_ordered.append(Like.objects.filter(worthySecret = i).count())

    # secret_index = []
    # for j in secret_content_ordered:
    #     secret_index.append(j.id)

    posted = []
    liked = []
    post_bool = {}
    like_bool = {}
    steez_list = []
    keyz_list = []

    for x in range(len(secret_content_ordered),0,-1):
        secret_check1 = Secret.objects.filter(id = secret_content_ordered[x-1].id).values('secret_maker').annotate(Count('secret_maker'))
        secret_check2 = User.objects.filter(id=id).values('id').annotate(Count('id'))
        if secret_check1.exists():
            if secret_check1[0]['secret_maker'] == secret_check2[0]['id']:

                posted = []
                poster = "You posted this"
                posted.append(poster)
                this_id = secret_content_ordered[x-1].id
                post_bool[this_id] = True

    for y in range(len(secret_content_ordered), 0, -1):

        # Like.objects.filter(worthySecret = Secret.objects.get(id = secret_content_ordered[y].id)).values('liker').annotate(Count('liker'))
        liker_check1 = Like.objects.filter(worthySecret = Secret.objects.get(id = secret_content_ordered[y-1].id)).values('liker').annotate(Count('liker'))
        liker_check2 = User.objects.filter(id=id).values('id').annotate(Count('id'))
        if liker_check1.exists():
            for i, c in enumerate(liker_check1):
                if c['liker'] == liker_check2[0]['id']:
                    liked = []
                    likey = 'you liked this'
                    liked.append(likey)
                    this_id = secret_content_ordered[y-1].id
                    like_bool[this_id] = True

    for steez in post_bool:
        steez_list.append(steez)

    for keyz in like_bool:
        keyz_list.append(keyz)

    secret_popularity = zip(secret_likes_ordered, secret_content_ordered)
    secret_popularity_dict = dict(secret_popularity)
    od = collections.OrderedDict(reversed(sorted(secret_popularity_dict.items())))

    context = {
        'user': User.objects.get(id = id),
        'popularity_order': od,
        'poster2': posted,
        'likey2': liked,
        'post_bool': post_bool,
        'like_bool': like_bool,
        'keyz_list': keyz_list,
        'steez_list': steez_list
    }

    return render(request, 'first_app/popular.html', context)
