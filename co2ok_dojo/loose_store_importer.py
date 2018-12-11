from ninja_partner_stores.models import *

# class Command(BaseCommand):
def importer():
    store = Store.objects.create(website="ebay.nl", network="ebay", tussenstukje="1346-53482-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="nl")
    store.country.add(country)

    store = Store.objects.create(website="ebay.at", network="ebay", tussenstukje="5221-53469-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="at")
    store.country.add(country)

    store = Store.objects.create(website="ebay.com.au", network="ebay", tussenstukje="705-53470-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="au")
    store.country.add(country)    

    store = Store.objects.create(website="ebay.ca", network="ebay", tussenstukje="706-53473-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="ca")
    store.country.add(country)

    store = Store.objects.create(website="ebay.ch", network="ebay", tussenstukje="5222-53480-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="ch")
    store.country.add(country)

    store = Store.objects.create(website="ebay.de", network="ebay", tussenstukje="707-53477-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="de")
    store.country.add(country)

    store = Store.objects.create(website="ebay.es", network="ebay", tussenstukje="1185-53479-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="es")
    store.country.add(country)

    store = Store.objects.create(website="ebay.fr", network="ebay", tussenstukje="709-53476-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="fr")
    store.country.add(country)

    store = Store.objects.create(website="ebay.ie", network="ebay", tussenstukje="5282-53468-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="ie")
    store.country.add(country)

    store = Store.objects.create(website="ebay.it", network="ebay", tussenstukje="724-53478-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="it")
    store.country.add(country)

    store = Store.objects.create(website="ebay.co.uk", network="ebay", tussenstukje="710-53481-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="uk")
    store.country.add(country)

    store = Store.objects.create(website="ebay.com", network="ebay", tussenstukje="711-53200-19255-0")
    cat_names = ["Fashion", "Electronics", "Home, Garden & Pets", "Books & Media", "Hobby", "Vehicles", "Food", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="us")
    store.country.add(country)

    store = Store.objects.create(website="bol.com", network="bol")
    cat_names = ["Books & Media", "Electronics", "Sport & Recreation", "Fashion", "Home, Garden & Pets", "Toys", "Hobby", "Health", "Gifts & Gadgets"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country_codes = ["nl", "de"]
    for country_code in country_codes:
        country = Country.objects.get(code=country_code)
        store.country.add(country)

    try:
        store = Store.objects.get(website="dx.com")
        store.network="dx"
    except:
        store = Store.objects.create(website="dx.com", network="dx")
    cat_names = ["IT & Office", "Home, Garden & Pets", "Electronics", "Hobby", "Sport & Recreation", "Health", "Toys", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country_codes = ["nl", "de", "es", "us", "uk", "it", "fr"]
    for country_code in country_codes:
        country = Country.objects.get(code=country_code)
        store.country.add(country)

    store = Store.objects.create(website="coolblue.nl", network="coolblue", tussenstukje="1101l3r4E")
    cat_names = ["Electronics", "Home, Garden & Pets", "Fashion", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="nl")
    store.country.add(country)

    store = Store.objects.create(website="coolblue.be", network="coolblue", tussenstukje="1011l3qZq")
    cat_names = ["Electronics", "Home, Garden & Pets", "Fashion", "Other"]
    for cat_name in cat_names:
        cat = Category.objects.get(name=cat_name)
        store.category.add(cat)
    country = Country.objects.get(code="be")
    store.country.add(country)


    store = Store.objects.create(website="booking.com", network="booking")
    cat = Category.objects.get(name="Holiday")
    store.category.add(cat)
    country_codes = ["nl", "de", "es", "us", "uk", "it", "ca", "fr"]
    for country_code in country_codes:
        country = Country.objects.get(code=country_code)
        store.country.add(country)