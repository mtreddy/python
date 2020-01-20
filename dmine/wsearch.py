from googlesearch import search
from bs4 import BeautifulSoup
from requests import get
import requests_cache
import datetime

class wsearch:
    def __init__(self):
        tstr = "Tirumala Reddy Marri"

    def getLinks(self, tstr, tnum, tstop):
        links = []
        res = search(tstr, num=tnum, stop=tstop)
        for lnks in res:
            links.append(lnks)
        print(links)
        return links

    def scrapeWeb(self, tstr):
        text = []
        links = self.getLinks(tstr,10,10)
        for link in links:
            res = get(link)
            data = BeautifulSoup(res.text, 'html.parser')
            text.append(data.text)
        return text 

## Caching requests
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite',expire_after=expire_after)
ws = wsearch()
tdata = ws.scrapeWeb("google analyst rating")
print(tdata[0])
