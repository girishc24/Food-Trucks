from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import FoodTruckSerializer
from math import radians, sin, cos, sqrt, atan2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse("Welcome to Food Truck Locations")

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


@api_view(['GET'])
def foodtrucks(request):
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')
    
    if lat is None or lon is None:
        return Response(
            {"error": "Both 'latitude' and 'longitude' query parameters are required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return Response(
            {"error": "Invalid 'latitude' or 'longitude' format. They must be real numbers."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    food_trucks = Foodtruck.objects.all()
    print(f"Found {food_trucks.count()} food trucks in the database.")
    
    food_trucks = sorted(food_trucks, key=lambda truck: calculate_distance(lat, lon, truck.latitude, truck.longitude))
    nearest_food_trucks = food_trucks[:5]
    print(f"Nearest food trucks: {nearest_food_trucks}")
    
    serializer = FoodTruckSerializer(nearest_food_trucks, many=True)
    return Response(serializer.data)

