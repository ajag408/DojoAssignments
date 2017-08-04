from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index2$', views.index2),
    url(r'^index3$', views.index3),
    url(r'^new_lead$', views.add_lead),
    url(r'^edit_lead/(?P<lead_id>\d+)$', views.edit_lead),
    url(r'^filter(?P<page>\d+)$', views.filter)
]
