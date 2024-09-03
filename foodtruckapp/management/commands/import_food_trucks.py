import csv
from django.core.management.base import BaseCommand
from foodtruckapp.models import Foodtruck

class Command(BaseCommand):
    help = 'Load food truck data from a CSV file'

    def handle(self, *args, **options):
        with open('foodtruckapp/management/commands/food-truck-data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Foodtruck.objects.create(
                    locationid=row['locationid'],
                    applicant=row['Applicant'],
                    facility_type=row['FacilityType'],
                    cnn=row.get('CNN'),
                    location_description=row.get('LocationDescription'),
                    address=row['Address'],
                    block_lot=row.get('BlockLot'),
                    block=row.get('Block'),
                    lot=row.get('Lot'),
                    permit=row['permit'],
                    status=row['Status'],
                    food_items=row.get('FoodItems'),
                    latitude=float(row['Latitude']),
                    longitude=float(row['Longitude']),
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded food truck data'))
