from data_access.api.get_prices import *

ticker = 'NVDA'
date = '20150101'
frequency = 'daily'

test = from_barchart_historical_prices(ticker, date, frequency)
print(test)
