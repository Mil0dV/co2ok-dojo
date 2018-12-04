from django.urls import path

from . import views

app_name = 'partner_stores'
urlpatterns = [
    # ex: /store/
    path('', views.index, name='index'),
]