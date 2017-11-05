from API.get_holdings import *
from API.get_prices import *
from target_weights import *
import pandas as pd

etfs = pd.read_json('C:/_data/ETFs.txt')
holdings = from_sigfig()
prices = from_sigfig_stale_prices()
marked_portfolio = pd.merge(etfs, holdings, on='Symbol').merge(prices, on='Symbol')

marked_portfolio['Value'] = marked_portfolio['Shares'] * marked_portfolio['Last']
print(marked_portfolio)

target_portfolio = equal_weight(marked_portfolio)
print(target_portfolio)
