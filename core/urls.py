
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insertar/pelicula/', views.insertar_pelicula, name='insertar_pelicula'),
    path('insertar/director/', views.insertar_director, name='insertar_director'),
    path('insertar/genero/', views.insertar_genero, name='insertar_genero'),
    path('buscar/', views.buscar_pelicula, name='buscar_pelicula'),
]
