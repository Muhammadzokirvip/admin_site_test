from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('banner-list/', views.list_banner),
    path('banner-create/', views.create_banner),
    path('service-list/', views.list_service),
    path('service-create/', views.create_service),
    path('aboutus-list/', views.list_aboutus),
    path('aboutus-create/', views.create_aboutus),
    path('price-list/', views.list_price),
    path('price-create/', views.create_price),
]