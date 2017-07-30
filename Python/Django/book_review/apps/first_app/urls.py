from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^reg$', views.validate_register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^review_home$', views.review_home),
    url(r'^new_two$', views.new_two),
    url(r'^add_book$', views.add_book),
    url(r'^add_review/(?P<this_book_id>\d+)/(?P<user_id>\d+)$', views.add_review),
    url(r'^render_book_page/(?P<book_render_id>\d+)$', views.render_book_page),
    url(r'^render_user_page/(?P<user_render_id>\d+)$', views.render_user_page)
]
