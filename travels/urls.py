from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list, name='travel_list'),
    path('create/', views.travel_create, name='travel_create'),
    path('<int:pk>/', views.travel_detail, name='travel_detail'),
]
