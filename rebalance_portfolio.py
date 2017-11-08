from API.get_holdings import *
from API.get_prices import *
from target_weights import *
import pandas as pd
import math


etfs = pd.read_json('C:/_data/ETFs.txt')
holdings = from_sigfig()
prices = from_barchart() # TODO add some error handling for bad requests to api
marked_portfolio = pd.merge(etfs, holdings, on='Symbol').merge(prices, left_on='Symbol', right_on='symbol')
marked_portfolio['Value'] = marked_portfolio['Shares'] * marked_portfolio['lastPrice']
target_portfolio = equal_weight(marked_portfolio)
target_portfolio['TargetShares'] = (target_portfolio['TargetValue'] / target_portfolio['lastPrice']).round(0)
print(target_portfolio)
