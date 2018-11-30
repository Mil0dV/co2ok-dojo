from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Store
from .functions import *
# Create your views here.

def index(request):
    latest_stores_list = Store.objects.order_by('-pub_date')
    websites = []
    for f in latest_stores_list:
        website = "http://www." + str(f) + "/"
        websites.append(website)
        print(websites)
        # return website
    context = {
        'latest_store_list' : websites
    }
    print(context)
   
    return render(request, 'stores/index.html', context)
