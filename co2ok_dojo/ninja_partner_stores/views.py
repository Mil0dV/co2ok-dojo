from django.shortcuts import render
from django.utils.translation import ugettext as _

from .forms import SearchForm
from .models import Store

def partner_stores(request):

    # form = SearchForm(request.POST)
    if request.method == "GET":

        # search_value = form.cleaned_data['search_field']
        search_value = request.GET.get('query', None)
        search_result = Store.objects.filter(website=search_value)
        # search_result_count = search_result.count()
        #
        # if search_result_count > 0:
        #     return search_result
        # else:
        #     search_result = _("nieks gevonden")

        return render(request, "ninja_partner_stores/ninja-partner-stores.html", {'search_results': search_result, 'search_value':search_value})

    return render(request, "ninja_partner_stores/ninja-partner-stores.html",{})
