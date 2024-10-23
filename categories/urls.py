from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
]
