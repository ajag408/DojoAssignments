from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users_home),
    url(r'^users/new$', views.render_add_user),
    url(r'^users/create$', views.add_user)
]
