
import requests
from bs4 import BeautifulSoup

link = "https://www.greenlight.guru/blog/top-100-medical-device-companies"
page = requests.get(link)
soup = BeautifulSoup(page.content,"html.parser")
table = soup.table
tr = table.find_all('tr')
htable = []
for tb in tr:
     td = tb.find_all('td')
     row = [i.text for i in td]
     htable.append(row)
     print(row)

