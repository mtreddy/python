import sys
import re
import os
from bs4 import BeautifulSoup 
from requests import get
import requests_cache

## AMD part number EX "EPYC 7662"
## Vendor Dell, ASUS, Lenovo etc
## down load results?
## get specint schore?
class minespec:
    def findIntScoreForId(self, lst, Id):
        data = []
        pattrn = r'EPYC %s' % (Id)
        for itm in lst:
            if len(re.findall(pattrn,itm.text)) != 0:
                tag = itm.find_all("td");
                #print("\n")
                ddict = {}
                for score in tag:
                    if score.attrs['class'][0] == "test_sponsor":
                        ddict['Test Sponsor  :'] = score.text
                        #print("Test Sponsor  :%s" % (score.text))
                    if score.attrs['class'][0] == "hw_model":
                        ddict['HW Model      :'] =  score.text.split("\n")[0]
                        #print("HW Model      :%s" % (score.text.split("\n")[0]))
                    if score.attrs['class'][0] == "basemean":
                        ddict['Basemean      :'] = (re.findall(r'\d+',score.text)[0])
                        #print("basemean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "peakmean" and (len(re.findall(r'\d+',score.text)) != 0):
                        ddict['Peakmean      :'] = (re.findall(r'\d+',score.text)[0])
                        #print("peakmean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "base_copies":
                        ddict['Copeis        :'] = (re.findall(r'\d+',score.text)[0])
                        #print("Copies        :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_ncores":
                        ddict['No of Cores   :'] = (re.findall(r'\d+',score.text)[0])
                        #print("No of Cores   :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_nchips":
                        ddict['No of Sockets   :'] = (re.findall(r'\d+',score.text)[0])
                        #print("No of Sockets :%s" % (re.findall(r'\d+',score.text)[0]))
                data.append(ddict)
        return data
    ## Function which takes Vendor name as ibput and dumps different part-ids and scores
    def findIntForVendorId(self, lst, vId):
        data = []
        pattrn = r'%s' % (vId)
        for itm in lst:
            if (len(re.findall(r'EPYC',itm.text)) != 0) and (len(re.findall(pattrn,itm.text)) != 0):
                tag = itm.find_all("td");
                #print("\n")
                ddict = {}
                for score in tag:
                    if score.attrs['class'][0] == "test_sponsor":
                        ddict['Test Sponsor  :'] = score.text
                        #print("Test Sponsor  :%s" % (score.text))
                    if score.attrs['class'][0] == "hw_model":
                        ddict['HW Model      :'] =  score.text.split("\n")[0]
                        #print("HW Model      :%s" % (score.text.split("\n")[0]))
                    if score.attrs['class'][0] == "basemean":
                        ddict['Basemean      :'] = (re.findall(r'\d+',score.text)[0])
                        #print("basemean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "peakmean" and (len(re.findall(r'\d+',score.text)) != 0):
                        ddict['Peakmean      :'] = (re.findall(r'\d+',score.text)[0])
                        #print("peakmean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "base_copies":
                        ddict['Copeis        :'] = (re.findall(r'\d+',score.text)[0])
                        #print("Copies        :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_ncores":
                        ddict['No of Cores   :'] = (re.findall(r'\d+',score.text)[0])
                        #print("No of Cores   :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_nchips":
                        ddict['No of Sockets   :'] = (re.findall(r'\d+',score.text)[0])
                        #print("No of Sockets :%s" % (re.findall(r'\d+',score.text)[0]))
                data.append(ddict)
        return data
    ## Function which takes Vendor name as ibput and dumps different part-ids and scores
    def findIntForChipsVendorId(self, lst, vId):
        data = []
        pattrn = r'%s' % (vId)
        for itm in lst:
            if (len(re.findall(pattrn,itm.text)) != 0):
                tag = itm.find_all("td");
                #print("\n")
                ddict = {}
                for score in tag:
                    if score.attrs['class'][0] == "test_sponsor":
                        ddict['Test Sponsor  :'] = score.text
                        #print("Test Sponsor  :%s" % (score.text))
                    if score.attrs['class'][0] == "hw_model":
                        ddict['HW Model      :'] =  score.text.split("\n")[0]
                        #print("HW Model      :%s" % (score.text.split("\n")[0]))
                    if score.attrs['class'][0] == "basemean":
                        ddict['Basemean      :'] = (re.findall(r'\d+',score.text)[0])
                        #print("basemean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "peakmean" and (len(re.findall(r'\d+',score.text)) != 0):
                        ddict['Peakmean      :'] = (re.findall(r'\d+',score.text)[0])
                        #print("peakmean      :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "base_copies":
                        ddict['Copeis        :'] = (re.findall(r'\d+',score.text)[0])
                        #print("Copies        :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_ncores":
                        ddict['No of Cores   :'] = (re.findall(r'\d+',score.text)[0])
                        #print("No of Cores   :%s" % (re.findall(r'\d+',score.text)[0]))
                    if score.attrs['class'][0] == "hw_nchips":
                        ddict['No of Sockets   :'] = (re.findall(r'\d+',score.text)[0])
                        #print("No of Sockets :%s" % (re.findall(r'\d+',score.text)[0]))
                data.append(ddict)
        return data
    ## Function to download SPECINT text file.
    ## Criteria need to be unique, If it finds more than one result 
    ## no result file will be downloaded
    ## criteria = {'test_sponsor':'Dell', 'core_id':'7662', 'hw_chips': '2', 'base_copies':'128'}
    def anlyzeSPecIntTextResults(self, lst, vId ):
        data = []
        links = []
        base = 'https://www.spec.org/cpu2017/results/'
        pattrn = r'%s' % (vId)
        for itm in lst:
            if (len(re.findall(r'EPYC',itm.text)) != 0) and (len(re.findall(pattrn,itm.text)) != 0):
                tag = itm.find_all("td");
                if len(tag) == 0:
                    continue
                for link in tag:
                    if len(link) == 0:
                        continue
                    tt = link.find_all("a")
                    if len(tt) == 0:
                        continue
                    tlink = base + tt[2].attrs['href']
                    links.append(tlink)
        for link in links:
            htm = get(link)
            soup = BeautifulSoup(htm.text, 'html.parser')
            data.append(soup)

        #print(data)
        return data



    ## Function to analyze SPECINT results
    def analyzeSpectIntResults(self, txtFile):
        print("Need to implement")

## This will need part number
url = "https://www.spec.org/cpu2017/results/rint2017.html"
rlink = "https://www.spec.org/cpu2017/results/"
requests_cache.install_cache('specint_cache', backend='sqlite', expire_after=180)
res = get(url)
soup = BeautifulSoup(res.text, "html.parser")

lst = soup.find_all("tr")
print(len(lst))

specint = minespec()
#ids = specint.findIntScoreForId(lst,Id="7542")
#print(ids)
#vids = specint.findIntForVendorId(lst,vId="ASUS")
#print(vids[1])
data = specint.anlyzeSPecIntTextResults(lst,vId="7542")
