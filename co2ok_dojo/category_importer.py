import csv
# from django.core.management.base import BaseCommand

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():

     categories = [

       'Clothing',
       'Electronics',
       'Books & Media',
       'Presents & Gadgets',
       'Food & Drinks',
       'Health',
       'Sports & Recreation',
       'Holiday',
       'Fashion & Jewelry',
       'Toys',
       'Dating',
       'Erotica',
       'House & Garden & Animals',
       'IT & Office',
       'Vehicles',
       'Department stores',
       'Other'

     ]

     countries = [

       'nl',
       'fr',
       'de',
       'es',
       'en'

     ]
    # ###### Categories maken:
    for cat_name in categories:
        Category.objects.create(name=cat_name)

    # ###### Countries maken:
    for country_code in countries:
        Category.objects.create(name=country_code)
