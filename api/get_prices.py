import json
import requests
import pandas as pd


def from_sigfig_stale_prices():
    return_fields = ['Symbol', 'Last']
    prices = pd.read_csv('C:/_data/Portfolios.csv', usecols=return_fields)\
        .drop_duplicates(subset=['Symbol', 'Last'], keep='first')
    return prices


def from_barchart():
    params = open('C:/_data/BarchartApiKeyAndSymbols.txt', 'r').read()
    response = requests.get('http://marketdata.websol.barchart.com/getQuote.json', params=params)
    status = response.status_code
    if status == 200:
        prices = pd.read_json(json.dumps(response.json()['results']))
        return prices[['symbol', 'lastPrice']]
    else: # TODO best way to handle errors?
        error = status
        return error
