from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^register$', views.reg),
    url(r'^login$', views.login),
    url(r'^users/new$', views.reg),
    url(r'^users$', views.all)
]
