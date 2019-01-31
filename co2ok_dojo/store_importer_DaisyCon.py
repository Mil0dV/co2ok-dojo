import csv
from django.core.management.base import BaseCommand

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():
    country_code = "nl"

    with open('daisy.csv') as csvfile:
        # readCS = csv.DictReader(csvfile, fieldnames='website', restkey='categories', delimiter='|')
        readCS = csv.reader(csvfile, delimiter=';')

        for row in readCS:
            splitedurl = row[0].split('/')
            moresplited = splitedurl[4].split('=')
            tussenstuktwee = moresplited[1].split('&')
            tussenstukdrie = moresplited[2].split('&')
            # print(row[0])
            site_name = row[1]
            # print(row[1:])
            try:
                store = Store.objects.get(website=site_name)
            except:
                # pass
                store = Store.objects.create(website=site_name, network="daisy", tussenstukje=splitedurl[2], tussenstukjetwee=tussenstuktwee[0], tussenstukjedrie=tussenstukdrie[0])
                # print(middle_name, row6[0])
            # print("gelukt! " + store.website)
            country = Country.objects.get(code=country_code)
            store.country.add(country)
            cat_name = row[2]
            cat = Category.objects.get(name=cat_name)
            store.category.add(cat)
            # print("Gelukt " + store.category)
            # print(row)
            # website = row['website']
            # row2 = row[0].split('/')
            # row3 = row2[-1].split('?')
            # row4 = row3[-1].split('=')
            # row5 = row4[-1].split('_')
            # print('"' + row2[0] + '" => array("{}'.format('/'.join(row2[0:-1]))  + '", "' + row5[0] + '"),')
            # # for de categorien
            # # for de countries



# ###### Categories maken:
# ###### NB moet nu Duits
# for cat_name in categories:
#     Category.objects.create(name=cat_name)
