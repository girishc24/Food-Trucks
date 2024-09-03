from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nearest-food-trucks-location/', views.foodtrucks, name='nearest_food_trucks_location'),
]