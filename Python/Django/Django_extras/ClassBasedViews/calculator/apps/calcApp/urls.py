from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.Calculator.as_view())     # This line has changed!
]
