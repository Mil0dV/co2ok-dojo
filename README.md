# co2ok-dojo

1. pipenv install
1. pipenv shell
1. .env aan maken
1. in de .env file de keys doen (om vragen)
1. `python manage.py migrate && python manage.py runserver`


1. python manage.py shell{
  from category_importer import *
  importer()

  from yk_importer import *
  importer()

  from loose_store_importer import *
  importer()

  from store_importer_TradeTracker import *
  importer()
}

Wat iig nog extra nodig is in de requirements:
django-environ social-auth-app-django
django-sslserver #dev

SSL zou je dan moeten kunnen draaien met
`python manage.py runsslserver`
