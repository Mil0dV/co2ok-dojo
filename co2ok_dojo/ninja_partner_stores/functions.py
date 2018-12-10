from .models import Store
import re

class Url_filter():
    def uri_encode(store):
        regex = re.search('[^/]*/[^/]*/[^/]*/[^/]*/(.*)$', store.website)
        print(regex)
        return regex.group(1)

    def makeURLlink(store):
        # print("http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + url + "%2Fapi_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja")
        if(store.network == "awin"):
            return "http://www.awin1.com/cread.php?awinmid=http%3A%2F%2F" + store.tussenstukje + "&awinaffid=533371&clickref=chex&p=http%3A%2F%2F" + store.website + "%2F"
        elif(store.website == "bol.com"):
            return "https://partner.bol.com/click/click?p=2&t=url&s=51851&f=TXL&url=http%3A%2F%2F" + store.website + "%2F"
        elif(store.website == "coolblue"):
            return "https://prf.hn/click/camref:" + store.tussenstukje + "/destination:http%3A%2F%2F" + store.website + "%2F"
        elif(store.website == "ebay"):
            return "http://rover.ebay.com/rover/1/" + store.tussenstukje + "/1?ff3=4&pub=5575349754&toolid=11800&campid=5338219191&customid=chex&mpre=http%3A%2F%2F" + store.website + "%2F"
        elif(store.website == "dx.com"):
            return store.website + "?TC=USD&&Utm_rid=78139600&Utm_source=affiliate"
        elif(store.website == "booking.com"):
            return "http://booking.com?aid=1627502&label=chex"
        elif(store.network == "tc.tradetracker"):
            return "http://tc.tradetracker.net/?c=" + store.tussenstukje + "&m=12&a=315369&u="
        elif(store.network == "tradetracker"):
            return "https://www." + store.website + "/" + store.tussenstukje + "/?tt=" + store.tussenstukjetwee + "_0_315369_"
        elif(store.network == "yieldkit"):
            return "http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + store.website + "%2Fapi_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja"
