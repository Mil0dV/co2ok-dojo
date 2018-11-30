from django.urls import path

from . import views

app_name = 'partner_stores'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]