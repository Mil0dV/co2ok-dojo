from .models import Store
import re

def uri_encode(url):
    Regex = re.search('[^/]*/[^/]*/[^/]*/[^/]*/(.*)$', url)
    return Regex.group(1)

def readArraySite(url):
    # print("http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + url + "%2Fapi_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja")
    if(Network == "awin"):
        return "http://www.awin1.com/cread.php?awinmid=http%3A%2F%2F" + Tussenstukjes + "&awinaffid=533371&clickref=chex&p=http%3A%2F%2F" + url + "%2F"
    elif(Website == "bol"):
        return "https://partner.bol.com/click/click?p=2&t=url&s=51851&f=TXL&url=http%3A%2F%2F" + url + "%2F"
    elif(Website == "coolblue"):
        return "https://prf.hn/click/camref:" + Tussenstukjes + "/destination:http%3A%2F%2F" + url + "%2F"
    elif(Website == "ebay"):
        return "http://rover.ebay.com/rover/1/" + Land + "/1?ff3=4&pub=5575349754&toolid=11800&campid=5338219191&customid=chex&mpre=http%3A%2F%2F" + url + "%2F"
    elif(Website == "dx"):
        return url + "?TC=USD&&Utm_rid=78139600&Utm_source=affiliate"
    elif(Website == "booking"):
        return "http://booking.com?aid=1627502&label=chex"
    elif(Netwerk == "tc.tradetracker"):
        return "http://tc.tradetracker.net/?c=" + Tussenstukjes + "&m=12&a=315369&u=" + uri_encode(url)
    elif(Netwerk == "tradetracker"):
        return url + Tussenstukjes[0] + "/?tt=" + Tussenstukjes[1] + "_0_315369_"
    elif(Netwerk == "yieldkit"):
        return "http://r.srvtrck.com/v1/redirect?url=http%3A%2F%2F" + url + "%2Fapi_key=6192753faa5975d8d9450690274e77dd&site_id=249c53bccf944c4c8f010cf6c914f30c&type=url&source=https%3A%2F%2Fco2ok.ninja"