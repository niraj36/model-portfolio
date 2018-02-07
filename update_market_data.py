import data_access

# TODO Query the database to identify all distinct tickers and the last date they were updated
ticker = 'NVDA'
date = '20150101'
frequency = 'daily'

test = data_access.api.get_prices.from_barchart_historical_prices(ticker, date, frequency)
print(test)
