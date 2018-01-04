import json
import requests
import pandas as pd


# Gets prices from last holdings report
def from_sigfig_stale_prices():
    return_fields = ['Symbol', 'Last']
    prices = pd.read_csv('C:/_data/Portfolios.csv', usecols=return_fields)\
        .drop_duplicates(subset=['Symbol', 'Last'], keep='first')
    return prices


# Gets last traded price
# TODO refactor so the function can take in a list of tickers
def from_barchart_current_quote():
    params = open('C:/_data/BarchartApiKeyAndSymbols.txt', 'r').read()
    response = requests.get('http://marketdata.websol.barchart.com/getQuote.json', params=params)
    status = response.status_code

    if status == 200:
        quotes = pd.read_json(json.dumps(response.json()['results']))
        return quotes[['symbol', 'lastPrice']]
    else: # TODO best way to handle errors?
        error = status
        return error


# Gets historical prices for a given ticker and from a given date
def from_barchart_historical_prices(ticker, date, frequency):
    api_key = open('C:/_data/BarchartApiKey.txt', 'r').read()
    symbol = 'symbol='+ticker
    type = 'type='+frequency
    start_date = 'startDate='+date
    params = api_key+'&'+symbol+'&'+type+'&'+start_date
    response = requests.get('http://marketdata.websol.barchart.com/getHistory.json', params=params)
    status = response.status_code

    if status == 200:
        historical_prices = pd.read_json(json.dumps(response.json()['results']))
        return historical_prices[['symbol', 'tradingDay', 'close']]
    else:
        error = status # TODO need better error handling.
        return error
