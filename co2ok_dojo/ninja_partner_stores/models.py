import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code

class Store(models.Model):
    website = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    country = models.ManyToManyField(Country)
    network = models.CharField(max_length=200)
    tussenstukje = models.CharField(max_length=200)

    def __str__(self):
        return self.website
