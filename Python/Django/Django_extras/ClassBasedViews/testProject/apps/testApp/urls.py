# # option 1
# from django.conf.urls import url
# from . import views
# urlpatterns = [
#     url(r'^$', views.ExtendExample.as_view(), name = 'index'),
# ]
# option2
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.ExtendExample.as_view(footerText="bananaPhone"), name = 'index'),
]
