import csv
from django.core.management.base import BaseCommand

from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():
    country_code = "nl"

    with open('TradetrackerTest.csv') as csvfile:
        # readCS = csv.DictReader(csvfile, fieldnames='website', restkey='categories', delimiter='|')
        readCS = csv.reader(csvfile)

        for row in readCS:
            tradetrackerrow = row[0].split(';')
            tradetracker = tradetrackerrow[1].split('/')
            print(tradetrackerrow[2])
            if(tradetracker[2] == "tc.tradetracker.net"):

                splitedCSV = row[0].split(';')
                splited_url = splitedCSV[1].split('=')
                middle_name = splited_url[1].split('&')
                # print(row[0])
                site_name = splitedCSV[0]
                # print(row[1:])
                # print(site_name, middle_name[0])
                try:
                    store = Store.objects.get(website=site_name)
                    # print(site_name, middle_name[0])
                except:
                    # print(site_name, middle_name[0])
                    # pass
                    store = Store.objects.create(website=site_name, network="tc.tradetracker", tussenstukje=middle_name[0])
                print("gelukt! " + store.website)
            else:
                splitedCSV = row[0].split(';')
                splited_url = splitedCSV[1].split('/')
                moresplited = splited_url[-1].split('?')
                evenMoreSplitedURL = moresplited[-1].split('=')
                TheLastSplitedURL = evenMoreSplitedURL[-1].split('_')
                middle_name = '{}'.format('/'.join(splited_url[3:-1]))
                # print(row[0])
                site_name = splitedCSV[0]
                # print(row[1:])
                try:
                    store = Store.objects.get(website=site_name)
                except:
                    # pass
                    store = Store.objects.create(website=site_name, network="tradetracker", tussenstukje=middle_name, tussenstukjetwee=TheLastSplitedURL[0])
                    # print(middle_name, row6[0])
                print("gelukt! " + store.website)
            country = Country.objects.get(code=country_code)
            store.country.add(country)
            cat_name = tradetrackerrow[2]
            cat = Category.objects.get(name=cat_name)
            store.category.add(cat)
            print("Gelukt " + store.website + ", " + store.category) 
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
