from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='StudioGhibli-Home'),
    path('about/', views.about, name='StudioGhibli-About'),
]
