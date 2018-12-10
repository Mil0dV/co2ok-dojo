import csv
# from django.core.management.base import BaseCommand

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():

    categories = [

    'Books & Media',
    'Department Stores',
    'Electronics',
    'Erotica',
    'Fashion',
    'Dating',
    'Gifts & Gadgets',
    'Food',
    'Health',
    'Hobby',
    'Home, Garden & Pets',
    'Holiday',
    'IT & Office',
    'Presents & Gadgets',
    'Sport & Recreation',
    'Toys',
    'Party',
    'Vehicles',
    'Other'

    ]

    countries = [

    'nl',
    'fr',
    'de',
    'es',
    'us'

    ]
    # ###### Categories maken:
    for cat_name in categories:
        Category.objects.create(name=cat_name)

    # ###### Countries maken:
    for country_code in countries:
        Country.objects.create(code=country_code)
