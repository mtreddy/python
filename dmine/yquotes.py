import csv
from requests import get
from bs4 import BeautifulSoup

class yf:
    def collect_data(self, link):
        ht = get(link)
        soup = BeautifulSoup(ht.text, 'html.parser')
        # you need to know htmpl page info and find what string you looking for
        # here we are looking for "tr class="simpTblRow "
        slist = soup.find_all("tr", class_="simpTblRow")
        with open("test.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ticker", "Name", "Price", " Change", "% Change", "Volume", "Avg Vol", "Market Cap", "PE"])
            # slit gives is info on each ticker. But you need to extract necessary info
            for i in range(0,len(slist)-1):
                # we look for "td" 
                sfield = slist[i].find_all("td")
                # sfield has info on name, price, chage, %change, volume, avg volume, market cap
                writer.writerow([sfield[0].text,sfield[1].text,sfield[2].text,sfield[3].text,sfield[4].text,sfield[5].text,sfield[6].text,sfield[7].text,sfield[8].text])
url = "https://finance.yahoo.com/screener/predefined/undervalued_growth_stocks"

quotes = yf()

quotes.collect_data(url)
