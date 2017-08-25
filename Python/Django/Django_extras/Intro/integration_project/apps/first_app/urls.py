from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^reg$', views.validate_register),
    url(r'^login$', views.login),
    url(r'^logout', views.logout)
]
