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

            
stock = 'AMD'
link = ("https://finance.yahoo.com/quote/AMD/history?p=" + stock)
htm = get(link)
sp = BeautifulSoup(htm.text, 'html.parser')

tables = sp.findAll('table', {"class" : 'historical-prices'})

            
stock = 'AMD'
link = ("https://finance.yahoo.com/quote/AMD/history?p=" + stock)
htm = get(link)
sp = BeautifulSoup(htm.text, 'html.parser')

tables = sp.findAll('table', {"data-test":'historical-prices'})
print(len(tables))
th = tables[0].find('thead')
thnames = th.find_all('tr')
for tname in thnames:
    thname = th.find_all('span')
    thname = [cell.text.strip() for cell in thname]
    print(thname)
tbody = tables[0].find('tbody')
len(tbody)
rows = tbody.find_all('tr')
len(rows)
for row in rows:
    col = row.find_all('span')
    col = [cell.text.strip() for cell in col]
    print(col)
        