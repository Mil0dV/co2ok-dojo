from django.db import models
    #Zoekt naar bijv. ebay.nl(voor ebay alleen) en niks er voor of er na
    #def FindTLD(url):
    #    return s[s.find('ebay')+4:].split('/')[0]

    #Zoekt naar de .land voor ebay(en ebay alleen)
    #def readArray(url):
    #    tld = FindTLD(url)

    #    land_code = []

    #    switcher???

    #Zoekt naar bijv. drogisterij.net en niks er voor of er na
    #def FindSiteName(url):
    #    match = re.search('', url)
    #    return match.group(0)

    #Zoekt naar bijv. www.drogisterij.net en niks er voor of er na
    #def FindURLplusTLD(url):
    #    match = re.search('', url)
    #    return str.replace('www.', '', 1)

    #Zoekt naar https://drogisterij.net/ en niks er na
    #def FindURI(url):
    #    match = re.search('', url)
    #    return match.group(0)

    #
    #def readArraySite(url, strip_url):

    #    site = (FindURLplusTLD() ? FindURLplusTLD() : strip_url)

    #
    #def SubDomein(url):
    #    strip_url = url
    #    redir_url = readArraySite(url, strip_url)
    #    if redir_url == True:
    #        return redir_url
    #    else:
    #        return readArraySite(url, FindSiteName(url))
