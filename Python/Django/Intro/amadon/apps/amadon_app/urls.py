from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^buy/(?P<word>\w+)$', views.purchase),
    url(r'^checkout$', views.checkout)
]
