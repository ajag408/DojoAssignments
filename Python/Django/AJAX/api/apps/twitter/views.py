from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'twitter/home.html')

def tweets(request):
    print request.POST['name']
