import pandas as pd


def from_sigfig_stale_prices():
    return_fields = ['Symbol', 'Last']
    prices = pd.read_csv('C:/_data/Portfolios.csv', usecols=return_fields)\
        .drop_duplicates(subset=['Symbol', 'Last'], keep='first')
    return prices

# TODO add function to pull latest price from barchart api
'''
def from_barchart():
    # TODO parse api string components into token files in _data and update code to generate string from files
    prices = pd.read_json('http://marketdata.websol.barchart.com/getQuote.json?apikey=<ADD-KEY>&symbols=USMV,EEMV', orient='records')
    return prices
    print(prices)
'''
