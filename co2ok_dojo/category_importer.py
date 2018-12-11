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
    'us',
    'at',
    'uk',
    'be',
    'ca',
    'au',
    'ch',
    'ie',
    'it',

    ]
    # ###### Categories maken:
    for cat_name in categories:
        try:
            Category.objects.get(name=cat_name)
        except:
            Category.objects.create(name=cat_name)

    # ###### Countries maken:
    for country_code in countries:
        try:
            Country.objects.get(code=country_code)
        except:
            Country.objects.create(code=country_code)
