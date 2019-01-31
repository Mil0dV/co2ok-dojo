import datetime
from django.db import models
from django.utils import timezone
import urllib.parse


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
    tussenstukjetwee = models.CharField(max_length=200)
    tussenstukjedrie = models.CharField(max_length=200, default='')

    @property
    def makeURLlink(self):
        # print("http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + url + "%2Fapi_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja")
        if(self.network == "awin"):
            return "http://www.awin1.com/cread.php?awinmid=http%3A%2F%2F" + self.tussenstukje + "&awinaffid=533371&clickref=chex&p=http%3A%2F%2F" + self.website + "%2F"
        elif(self.network == "bol"):
            return "https://partner.bol.com/click/click?p=2&t=url&s=51851&f=TXL&url=http%3A%2F%2F" + self.website + "%2F"
        elif(self.network == "coolblue"):
            return "https://prf.hn/click/camref:" + self.tussenstukje + "/destination:http%3A%2F%2F" + self.website + "%2F"
        elif(self.network == "ebay"):
            return "http://rover.ebay.com/rover/1/" + self.tussenstukje + "/1?ff3=4&pub=5575349754&toolid=11800&campid=5338219191&customid=chex&mpre=http%3A%2F%2F" + self.website + "%2F"
        elif(self.network == "dx"):
            return "https://" + self.website + "?TC=USD&&Utm_rid=78139600&Utm_source=affiliate"
        elif(self.network == "booking"):
            return "http://booking.com?aid=1627502&label=chex"
        elif(self.network == "tc.tradetracker"):
            return "http://tc.tradetracker.net/?c=" + self.tussenstukje + "&m=12&a=315369&u="
        elif(self.network == "tradetracker"):
            return "https://www." + self.website + "/" + self.tussenstukje + "/?tt=" + self.tussenstukjetwee + "_0_315369_"
        elif(self.network == "yieldkit"):
            return "http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + self.website + "%2F&api_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja"

    def __str__(self):
        return str(self.website) + str(self.category.name)


    def makeredirectURLlink(self, url):
        network = getattr(self, 'network')
        encode = urllib.parse.quote_plus(url)
        uri_encode = urllib.parse.quote_plus("https://" + str(self.website) + "/")
        
        # print("http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + url + "%2Fapi_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja")
        if(self.network == "awin"):
            return "http://www.awin1.com/cread.php?awinmid=http%3A%2F%2F" + self.tussenstukje + "&awinaffid=533371&clickref=chex&p=http%3A%2F%2F" + encode + "%2F"
        elif(self.network == "bol"):
            return "https://partner.bol.com/click/click?p=2&t=url&s=51851&f=TXL&url=" + encode
        elif(self.network == "coolblue"):
            return "https://prf.hn/click/camref:" + self.tussenstukje + "/destination:" + encode
        elif(self.network == "ebay"):
            return "http://rover.ebay.com/rover/1/" + self.tussenstukje + "/1?ff3=4&pub=5575349754&toolid=11800&campid=5338219191&customid=chex&mpre=" + encode
        elif(self.network == "dx"):
            return "https://www." + self.website + "?TC=USD&&Utm_rid=78139600&Utm_source=affiliate"
        elif(self.network == "booking"):
            return "http://booking.com?aid=1627502&label=chex"
        elif(self.network == "anrdoezrs"):
            return 'http://www.anrdoezrs.net/links/8106588/type/dlg/sid/chex/' + encode
        elif(self.network == "cfjump"):
            return 'https://t.cfjump.com/50770/t/48059?Url=' + encode + '&UniqueId=chex'
        elif(self.network == "tc.tradetracker"):
            return "http://tc.tradetracker.net/?c=" + self.tussenstukje + "&m=12&a=315369&u=" + uri_encode
        elif(self.network == "daisy"):
            return "https://" + self.tussenstukje + "/c/?si=" + self.tussenstukjetwee + "&li=" + self.tussenstukjedrie + "&wi=303581&ws=&dl=" + uri_encode
        elif(self.network == "tradetracker"):
            return "https://www." + self.website + "/" + self.tussenstukje + "/?tt=" + self.tussenstukjetwee + "_0_315369_"
        elif(self.network == "yieldkit"):
            return "http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + encode + "%2F&api_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja"
        return "henk"


    def __str__(self):
        return str(self.website) + str(self.category.name)
