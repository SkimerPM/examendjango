from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurante_list, name='home'), 
    
    path('restaurantes/', views.restaurante_list, name='restaurante_list'),
    path('restaurantes/crear/', views.restaurante_create, name='restaurante_create'),
    path('restaurantes/editar/<int:pk>/', views.restaurante_update, name='restaurante_update'),
    path('restaurantes/eliminar/<int:pk>/', views.restaurante_delete, name='restaurante_delete'),
    
    # platos
    path('platos/', views.plato_list, name='plato_list'),
    path('platos/crear/', views.plato_create, name='plato_create'),
    path('platos/editar/<int:pk>/', views.plato_update, name='plato_update'),
    path('platos/eliminar/<int:pk>/', views.plato_delete, name='plato_delete'),
]