import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Store(models.Model):
    website = models.CharField(max_length=200)
    categories = models.CharField(max_length=800, blank=True)
    countries = models.CharField(max_length=200, blank=True)
    network = models.CharField(max_length=200)
    tussenstukje = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Website

    # heb dit erin laten staan als voorbeeldje:   
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class opnieuw maken om dan te migraten alles in een keer.
    
    


#(mini)Array lezen
    #array maken
#(mini)Array printen
    #print() gebruiken
#SVC inlezen
    #kijk naar je test ding met svc
    #Redirect links maken
        #Redirect in een array Tieven
#De redirect array inlezen
    #Redicert array maken
#De redirect array printen
    #print() gebruiken
    #links van maken
#Zoek Thingy maken
    #Land zoeken
    #Catogorie zoeken
#Netwerk met meeste geld boven aanzetten
    #awin boven dus
#import thing
