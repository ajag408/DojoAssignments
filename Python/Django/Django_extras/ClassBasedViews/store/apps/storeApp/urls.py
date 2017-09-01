from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^products$', views.Products.as_view()),
    url(r'^products/(?P<id>\d+)', views.Edit.as_view()),
    url(r'^delete/(?P<id>\d+)', views.delete)
]
