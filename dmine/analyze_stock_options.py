import os
import re
import sys
import datetime
from requests import get
import requests_cache
import pandas_datareader.data as web
from bs4 import BeautifulSoup 
# pip install requests_html
from yahoo_fin import options
from yahoo_fin import stock_info as si
class anaOptions:
    def __init__(self):
        data_sources = ["iex", "moex"]

    def getQuoteDateRange(self, quote, dsource, start, end, session):
        dt = web.DataReader(quote, dsource, start=start, end=end)
        return dt

    def getOptionDates(self, quote):
        nflx_dates = options.get_expiration_dates(quote)
        return nflx_dates
    
    def getOptionChain(self, quote, dates):
        chain = options.get_options_chain(quote, nflx_dates[0])
        return chain
    def getStrangle(self, ticker):
        chain = self.getOptionChain(ticker, ticker_dates[0])
        stock_price = si.get_live_price(ticker)
        col = chain["calls"].columns
        strk_price = chain["calls"][col[2]]
        indx = ''
        for ind in range(0,len(strk_price)-2):
            #print(strk_price[ind])
            if float(strk_price[ind]) <= stock_price and float(strk_price[ind+1])  >= stock_price:
                d1 = float(strk_price[ind]) - stock_price
                d2 = stock_price - float(strk_price[ind+1])
                if abs(d1) >= abs(d2):
                    indx = ind
                else:
                    indx = ind+1
        print("Stock Price %f" % (stock_price))
        print("Strike Price %f" % (strk_price[indx]))
        print("Call Price %f" % (float(chain["calls"][col[5]][indx])))
        print("Put Price %f" % (float(chain["puts"][col[5]][indx])))
        print("Pirce to pay for strangele %f" % ((float(chain["calls"][col[5]][indx])) + (float(chain["puts"][col[5]][indx]))))

    def getDateAfterEarnings(self, date):
        my_time = time.strptime(qtable['value'][8],'%b %d, %Y')
       
        d1 = time.mktime(my_time)
        after = ''
        before = ''
    
        for ds in ticker_dates:
            tt = "%s %s %s" % (ds.split()[0][0:3], ds.split()[1], ds.split()[2])
            my_time = time.strptime(tt, '%b %d, %Y')
            #print(my_time)
            td = time.mktime(my_time)
            if td >= d1:
                #print("Lower ")
                #print(qtable['value'][8], ds)
                after = td
                break
            else:
                #print("higher")
                #print(qtable['value'][8], ds)
                before = td
        date = datetime.datetime.fromtimestamp(1587106800.0)
        print(date)
        date = datetime.datetime.fromtimestamp(1587711600.0)
        print(date)
        qtable['value'][8]
        return (before, after)

expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

ticker = "NFLX"
opt = anaOptions()
ticker_dates = opt.getOptionDates(ticker)
print(ticker_dates)
#chain = opt.getOptionChain(ticker, ticker_dates[0])
sp = si.get_live_price(ticker)
opt.getStrangle(ticker)
qtable  = si.get_quote_table(ticker, dict_result = False)
analyst = si.get_analysts_info(ticker)
stats   = si.get_stats(ticker)
stock_holders = si.get_holders(ticker)
income_stmt = si.get_income_statement(ticker)
cash_flow = si.get_cash_flow(ticker)
data = si.get_data(ticker)
qtable = si.get_quote_table(ticker, dict_result = True)
#nasdaq_quotes = si.tickers_nasdaq()
#dow_quotes = si.tickers_nasdaq()
#from1999 = get_data('msft' , start_date = '01/01/1999')
#few_days = get_data('msft' , start_date = '01/01/1999' , end_date = '01/10/1999')
#ctive  = si.get_day_most_active()
#ainers = si.get_day_gainers()
#osers  = si.get_day_losers()