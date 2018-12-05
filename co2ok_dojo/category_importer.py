import csv
# from django.core.management.base import BaseCommand

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():

    # ###### Categories maken:
    for cat_name in categories:
        Category.objects.create(name=cat_name)







