from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('formulario', views.index, name='formulario'),
    path('productos', views.productos, name='productos'), 
    path('formulario', views.formulario, name='formulario'), 
]