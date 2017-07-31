from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html)
]
