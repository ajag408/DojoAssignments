from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_lead$', views.add_lead),
    url(r'^edit_lead/(?P<lead_id>\d+)$', views.edit_lead)
]
