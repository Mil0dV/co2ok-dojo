import csv

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():
    network_name = "linkpizza"
    # country_codes = ["nl", "de", "es", "us"]
    country_codes = ["nl"]

    for country_code in country_codes:
        with open('linkpizza_' + country_code + '.csv') as csvfile:
            # readCS = csv.DictReader(csvfile, fieldnames='website', restkey='categories', delimiter='|')
            readCS = csv.reader(csvfile, delimiter=';')
            for row in readCS:

                print(row[0])
                site_name = row[0]
            # for site_name in readCS:
                try: 
                    store = Store.objects.get(website=site_name)
                except:
                    store = Store.objects.create(website=site_name, network=network_name)
                print("gelukt! " + store.website)

                # # for de categorien
                print(row[1:])
                if len(row[1:]) > 0:
                    cat_name = row[1]
                    cat = Category.objects.get(name=cat_name)
                    store.category.add(cat)
                else:
                    print('No category found for ' + site_name)

                # for de countries
                country = Country.objects.get(code=country_code)
                store.country.add(country)
