from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('abm_s/', views.ABM_Stock),
    path('crear_stock/', views.crear_stock, name='crear_stock'),
    path('lista_stock/', views.lista_stock, name='lista_stock'),
    path('editar_stock/<int:pk>/', views.editar_stock, name='editar_stock'),
    path('eliminar_stock/<int:id>/', views.eliminar_stock, name='eliminar_stock'),# Aquí se corrige la vista a lista_stock
]
