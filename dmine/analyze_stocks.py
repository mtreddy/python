
import os
import sys
import datetime
import requests_cache
import pandas_datareader.data as web

class anaStocks:
    def __init__(self):
        data_sources = ["iex", "moex"]

    def getQuoteDateRange(self, quote, dsource, start, end, session):
        dt = web.DataReader(quote, dsource, start=start, end=end)
        return dt



expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

stocks = anaStocks()
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 1, 1)
data = stocks.getQuoteDateRange("AAPL", 'yahoo', start, end, session=session)
print(data[:10])

