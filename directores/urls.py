from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('peliculas/', views.peliculas, name='peliculas'),
    url('directores/', views.directores, name='directores'),
   
]