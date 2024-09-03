from django.db import models

# Create your models here.
class Foodtruck(models.Model):
    locationid = models.IntegerField()
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    cnn = models.CharField(max_length=255, null=True, blank=True)
    location_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=255, null=True, blank=True)
    block = models.CharField(max_length=255, null=True, blank=True)
    lot = models.CharField(max_length=255, null=True, blank=True)
    permit = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    food_items = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.applicant