from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import urllib.request
import urllib.parse
from urllib.parse import urlparse
from ninja_partner_stores.models import Store

# Create your views here.

def redirectURL(request):
    url = request.GET.get('url', None)

    urlParse = urlparse(url)

    urlSplit = urlParse.netloc.strip('www.')

    response = Store.objects.filter(website__startswith=urlSplit)[0].makeredirectURLlink(url)

    return HttpResponseRedirect(response)
