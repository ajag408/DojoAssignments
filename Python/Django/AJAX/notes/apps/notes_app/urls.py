from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_note$', views.add_note),
    url(r'^add_description/(?P<note_id>\d+)$', views.add_description),
    url(r'^delete/(?P<note_id>\d+)$', views.delete)
]
