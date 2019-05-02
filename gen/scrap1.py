from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    print(1)
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

if len(sys.argv) < 2 :
    link = 'http://www.pythonscraping.com/pages/page1.html'
else:
    link = sys.argv[1]
print(link)
title = getTitle(link)
if title == None:
    print('Title could not be found')
else:
    print(title)

