from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^reg$', views.validate_register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^home/(?P<id>\d+)$', views.home_render),
    url(r'^travel_plan_page/(?P<id>\d+)$', views.travel_plan_page),
    url(r'^add_plan/(?P<id>\d+)$', views.add_plan),
    url(r'^destination/(?P<id>\d+)$', views.destination_page),
    url(r'^join/(?P<id>\d+)$', views.join)
]
