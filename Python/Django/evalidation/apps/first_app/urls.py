from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^validate$', views.validate),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
