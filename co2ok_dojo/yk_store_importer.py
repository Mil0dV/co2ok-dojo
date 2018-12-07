import csv

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():
    network_name = "yieldkit"
    country_code = "nl"

    with open('yieldkit_nl.csv') as csvfile:
        # readCS = csv.DictReader(csvfile, fieldnames='website', restkey='categories', delimiter='|')
        readCS = csv.reader(csvfile, delimiter=';')

        for row in readCS:
            # print(row)
            # website = row['website']

            # row2 = row[0].split('/')
            # row3 = row2[-1].split('?')
            # row4 = row3[-1].split('=')
            # row5 = row4[-1].split('_')
            # print('"' + row2[0] + '" => array("{}'.format('/'.join(row2[0:-1]))  + '", "' + row5[0] + '"),')
            print(row[0])
            site_name = row[0]
            try: 
                store = Store.objects.get(website=site_name)
            except:
                store = Store.objects.create(website=site_name, network=network_name)
            print("gelukt! " + store.website)
            # # for de categorien
            print(row[1:])
            cat_name = row[1]
            cat = Category.objects.get(name=cat_name)
            store.category.add(cat)
            # for de countries
            country = Country.objects.get(code=country_code)
            store.country.add(country)







