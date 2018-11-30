import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Store(models.Model):
    website = models.CharField(max_length=200)
    categories = models.CharField(max_length=800)
    countries = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    tussenstukje = models.CharField(max_length=200)

    def __str__(self):
        return self.Website
