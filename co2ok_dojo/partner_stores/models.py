import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Store(models.Model):
    Website = models.CharField(max_length=200)
    Catogorie = models.CharField(max_length=200)
    Land = models.CharField(max_length=200)
    Netwerk = models.CharField(max_length=200)
    Tussenstukjes = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Website
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

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
