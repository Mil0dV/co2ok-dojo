from django.shortcuts import render

def ninja_partner_stores(request):
    return render(request, "ninja_partner_stores/ninja-partner-stores.html")
