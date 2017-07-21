from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'this_app/index.html')

def create_user(request):

   # we'll talk about the following two lines after we learn a little more
   # about forms
   if request.method == 'POST':
       if 'counter' not in request.session:
           request.session['counter'] = 1
       else:
           request.session['counter'] = int(request.session['counter']) + 1

       request.session['name']= request.POST['name']
       request.session['location']= request.POST['location']
       request.session['language'] = request.POST['language']
       request.session['comment'] = request.POST['comment']
       return redirect("/result")
   else:
       return redirect('/')

def show_user(request):
    return render(request, 'this_app/result.html')
