from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_word$', views.add_word),
    url(r'^clear$', views.clear_session)     
]