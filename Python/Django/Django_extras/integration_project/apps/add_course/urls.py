from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^users_courses$', views.users_courses),
    url(r'^add_user_course$', views.add_user_course),
    url(r'^courses$', views.add),
    url(r'^renderDelete/(?P<id>\d+)$', views.renderDelete),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^add_comment/(?P<id>\d+)$', views.add_comment)
]
