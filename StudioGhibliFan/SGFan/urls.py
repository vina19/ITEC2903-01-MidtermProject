from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='StudioGhibli-Home'),
    url(r'^list/$', views.movie_list, name='StudioGhibli-List'),
    url(r'^create/$', views.movie_create, name='StudioGhibli-Create'),
    url(r'^detail/(?P<id>\d+)/$', views.movie_detail, name='StudioGhibli-Detail'),
   	url(r'^update/$', views.movie_update, name='StudioGhibli-Update'),
   	url(r'^delete/$', views.movie_delete, name='StudioGhibli-Delete'),
]
