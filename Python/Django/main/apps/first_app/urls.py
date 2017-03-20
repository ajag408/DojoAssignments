from django.conf.urls import url
from . import views

def index(request):
    print ('8'*100)
    print ('bannanapeel')

urlpatterns = [
    url(r'^$', views.index)
]
