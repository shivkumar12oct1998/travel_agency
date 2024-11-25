# travel_package/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.travel_package_list, name='travel_package_list'),
    path('packages/<int:pk>/', views.travel_package_detail, name='travel_package_detail'),
    path('book/', views.booking_create, name='booking_create'),
    path('home/',views.home,name='home'),
     path('package/<int:pk>/', views.package_detail, name='package_detail'),
    #path('booking_confirmation/<int:pk>/', views.booking_confirmation, name='booking_confirmation'),
     path('booking_confirmation/<int:pk>/', views.booking_confirmation, name='booking_confirmation'),
]
