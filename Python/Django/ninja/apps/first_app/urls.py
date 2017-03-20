from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.almighty),
    url(r'^ninjas/(?P<color>\D+)$', views.solo)
]
