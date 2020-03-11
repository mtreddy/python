import os
import re
import sys
import datetime
from requests import get
import requests_cache
import pandas_datareader.data as web
from bs4 import BeautifulSoup 
from googlesearch import search


class salesResearch:
    def __init__(self):
        print("Initializing sales research")
    
    def getLinks(self, tstr):
        
        links = search(tstr,num=20,stop=20))
        for link in links:
            print(link)
        