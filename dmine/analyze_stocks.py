import os
import re
import sys
import datetime
from requests import get
import requests_cache
import pandas_datareader.data as web
from bs4 import BeautifulSoup 
from googlesearch import search

class anaStocks:
    def __init__(self):
        data_sources = ["iex", "moex"]

    def getQuoteDateRange(self, quote, dsource, start, end, session):
        dt = web.DataReader(quote, dsource, start=start, end=end)
        return dt

    def getQuoteInfo(self, quote):
        #first get link to yahoo finance
        tstr = "%s stock" % (quote)
        print(tstr)
        links = []
        lnk = ''
        res = search(tstr,num=10,stop=10)        
        for link in res:
            links.append(link)
        for link in links:
            if link.find("finance.yahoo.com\/quote") != -1:
                break
        print(link)
        #Then get data
        htm = get(link)
        sp = BeautifulSoup(htm.text,'html.parser')
        tr = sp.find_all("tbody")
        opn = 0
        cl = 0
        drange = 0
        mcap = 0
        PE = 0
        EPS = 0
        EDATES = ''


        for tag in tr:
            for val in tag:
                #print(val.text)
                pr = re.findall(r'Previous Close',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\.0-9]+',val.text)[0]
                    cl = float(pr[0])
                    print("close %s" % (cl))

                pr = re.findall(r'Open[0-9]+(.)[0-9]+',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\.0-9]+',val.text)[0]
                    opn = float(pr)
                    print("open %s" % (opn))

                pr = re.findall(r'(Day\'s Range)+',val.text)
                if len(pr) != 0:
                    pr =  val.text.split('Range')
                    print("days range %s" % (pr[1]))
               
                pr = re.findall(r'^(Volume)',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\,0-9]+',val.text)
                    print("Volume %s" % (pr[0]))

                pr = re.findall(r'(Market Cap)',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\.0-9]+',val.text)[0]
                    print("Market-cap %s" % (pr))
               
                pr = re.findall(r'(Beta \(5Y Monthly\))',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\.0-9]+',val.text)[1]
                    print("Beta %s" % (pr))

                pr = re.findall(r'(PE Ratio)',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\.0-9]+',val.text)
                    print("PE Ratio %s" % (pr[0]))

                pr = re.findall(r'(EPS)',val.text)
                if len(pr) != 0:
                    pr = re.findall(r'[\.0-9]+',val.text)
                    print("EPS %s" % (pr[0]))
                
                pr = re.findall(r'(Earnings Date)',val.text)
                if len(pr) != 0:
                    print(val.text)
                    pr = val.text.split("Date")
                    print("Earnings dates %s" % (pr[1]))
    def getRatings(self, quote):
        #first get link to yahoo finance
        tstr = "%s stock" % (quote)
        print(tstr)
        links = []
        lnk = ''
        res = search(tstr,num=10,stop=10)        
        for link in res:
            links.append(link)
        for link in links:
            if link.find("www.marketbeat.com") != -1:
                break
        print(link)
        #Then get data
        htm = get(link)
        sp = BeautifulSoup(htm.text,'html.parser')
        tr = sp.find_all("tbody")        
        for tag in tr:
            for val in tag:
                 print(val.text)                                
                                         
                     
                    
                    
                    
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

stocks = anaStocks()
#start = datetime.datetime(2018, 1, 1)
#end = datetime.datetime(2019, 1, 1)
#data = stocks.getQuoteDateRange("AAPL", 'yahoo', start, end, session=session)
#print(data[:10])

stocks.getQuoteInfo("AMD")

