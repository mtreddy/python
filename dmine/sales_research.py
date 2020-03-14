import os
import re
import sys
import datetime
from requests import get
import requests_cache
import pandas_datareader.data as web
from bs4 import BeautifulSoup 
from googlesearch import search
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
class salesResearch:
    def __init__(self):
        print("Initializing sales research")
    
    def getLinks(self, tstr):
        
        links = search(tstr,num=20,stop=20)
        for link in links:
            print(link)
        return links

sr = salesResearch()
links = sr.getLinks("B2B sales techniques")
for link in links:
    link = "https://www.saleshacker.com/b2b-sales-techniques/"
    htm = get(url=link, headers=headers)

    if htm.reason == "OK":
         sp = BeautifulSoup(htm.text,'html.parser')
         st = sp.findAll('p')
         len(st)
         for line in st:
            #print(line)
            print(line.text.strip())
