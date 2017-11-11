from api.get_holdings import *
from api.get_prices import *
from target_weights import *
from api.post_trades import *
import pandas as pd
import numpy as np

# Gather input data
etfs = pd.read_json('C:/_data/ETFs.txt') # investments subject to the rebalance
holdings = from_sigfig()
prices = from_barchart() # TODO add some error handling for bad requests to api

# Combine input data and calculate current portfolio value
marked_portfolio = pd.merge(etfs, holdings, on='Symbol').merge(prices, left_on='Symbol', right_on='symbol')
marked_portfolio['Value'] = marked_portfolio['Shares'] * marked_portfolio['lastPrice']

# Determine trades needed to get back to target weights
target_portfolio = equal_weight(marked_portfolio)
target_portfolio['TradeShares'] = ((target_portfolio['TargetValue'] - target_portfolio['Value'])
                                    / target_portfolio['lastPrice']).round(0)
target_portfolio['TradeDirection'] = np.where(target_portfolio['TradeShares'] > 0, 'BUY', 'SELL')

# Generate the trade blotter
to_csv(target_portfolio)
