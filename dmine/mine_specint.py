import sys
import re
import os
from bs4 import BeautifulSoup 
from requests import get

## AMD part number EX "EPYC 7662"
## Vendor Dell, ASUS, Lenovo etc
## down load results?
## get specint schore?
class minespec:
    def findIntScoreForId(self, lst, Id):
        pattrn = r'EPYC %s' % (Id)
        for itm in lst:
            if len(re.findall(pattrn,itm.text)) != 0:
                tag = itm.find_all("td");
                print("\n")
                for score in tag:
                    if score.attrs['class'][0] == "test_sponsor":
                        print("Test Sponsor  :%s" % (score.text))
                    if score.attrs['class'][0] == "basemean":
                        print("basemean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "peakmean":
                        print("peakmean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "base_copies":
                        print("Copies        :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_ncores":
                        print("No of Cores   :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_nchips":
                        print("No of Sockets :%s" % (re.findall(r'\d+',score.text)[0]))


                     




## This will need part number
url = "https://www.spec.org/cpu2017/results/rint2017.html"
rlink = "https://www.spec.org/cpu2017/results/"

res = get(url)
soup = BeautifulSoup(res.text, "html.parser")

lst = soup.find_all("tr")
print(len(lst))

ref = lst[3].find_all("a")

print(ref[2].attrs['href'])

for itm in lst:
     if len(re.findall(r'EPYC 7662',itm.text)) != 0:
         aa = itm.find_all("td");
         for a in aa:
             if a.text == 'Text':
                 print(a)


