from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^reg$', views.validate_register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^create_secret/(?P<id>\d+)$', views.create_secret),
    url(r'^like/(?P<id>\d+)$', views.like),
    url(r'^like2/(?P<id>\d+)$', views.like2),
    url(r'^delete1/(?P<id>\d+)$', views.delete1),
    url(r'^delete2/(?P<id>\d+)$', views.delete2),
    url(r'^secret_home/(?P<id>\d+)$', views.secret_home),
    url(r'^popular/(?P<id>\d+)$', views.popular)
]
