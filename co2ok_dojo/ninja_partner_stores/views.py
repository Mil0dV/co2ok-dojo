from django.shortcuts import render
from django.utils.translation import ugettext as _

from .forms import SearchForm
from .models import Store
import json

# def partner_stores(request):
#
#     # form = SearchForm(request.POST)
#     if request.method == "GET":
#
#         # search_value = form.cleaned_data['search_field']
#         search_value = request.GET.get('query', None)
#         search_result = Store.objects.filter(website=search_value)
#         search_result_count = search_result.count()
#
#         if search_result_count > 0:
#             search_result_found = search_result
#         else:
#             search_result = _("nieks gevonden")
#
#         return render(request, "ninja_partner_stores/ninja-partner-stores.html", {'search_results': search_result, 'search_value':search_value})
#
#     return render(request, "ninja_partner_stores/ninja-partner-stores.html",{})


def partner_stores(request):
    print('hoi')
    search_result = Store.objects.all()
    return render(request, "ninja_partner_stores/ninja-partner-stores.html",{'search_results': search_result})


def partner_stores_data(request):
    if request.method == 'GET':
        search_value = request.GET.get('search_val')
        search_result = Store.objects.filter(website__startswith=search_value)
        search_result_count = search_result.count()
        return render(request, "ninja_partner_stores/partner_stores_data.html",{'search_results': search_result, 'search_value':search_value, 'search_result_count':search_result_count})


def partner_stores_category(request):
    category_val = request.GET.get('category_val')
    category_result = Store.objects.filter(category__name=category_val)
    category_resultcount_count = category_result.count()
    return render(request, "ninja_partner_stores/partner_stores_data.html",{'category_results': category_result, 'category_resultcount_count':category_resultcount_count})
