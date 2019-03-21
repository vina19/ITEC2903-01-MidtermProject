from django.conf.urls import url
from django.contrib import admin
from .views import (
	movie_list,
	movie_create,
	movie_detail,
	movie_update,
	)

urlpatterns = [
    url(r'^$', movie_list, name='list'),
    url(r'^create/$', movie_create, name='create'),
    url(r'^(?P<id>\d+)/$', movie_detail, name='detail'),
   	url(r'^(?P<id>\d+)/edit/$', movie_update, name='update'),
]
