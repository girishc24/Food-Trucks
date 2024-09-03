from rest_framework import serializers
from .models import Foodtruck



class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodtruck
        fields = ['applicant', 'location_description', 'address', 'latitude', 'longitude', 'food_items','locationid']