import numpy as np
import pandas as pd
from data_access.api import get_holdings
from data_access.api import get_prices
from data_access.api import post_trades
import target_weights


# Gather input data
etfs = pd.read_json('C:/_data/ETFs.txt')  # holdings to rebalance
cash = pd.read_json('C:/_data/Cash.txt')  # cash symbol
holdings = get_holdings.from_sigfig()
prices = get_prices.from_barchart_current_quote()  # TODO add some error handling for bad requests to api

# Filter holdings to just ETFs and combine with recent prices
marked_portfolio = pd.merge(etfs, holdings, on='Symbol').merge(prices, left_on='Symbol', right_on='symbol')
marked_portfolio['Value'] = marked_portfolio['Shares'] * marked_portfolio['lastPrice']

# Add cash balances
cash_balance = pd.merge(cash, holdings, on='Symbol')
marked_portfolio = pd.concat([cash_balance, marked_portfolio])
marked_portfolio['Value'] = np.where(marked_portfolio['Value'].isnull(),
                                     marked_portfolio['Shares'], marked_portfolio['Value'])

# Determine trades needed to get back to target weights
target_portfolio = target_weights.equal_weight(marked_portfolio)
target_portfolio['TradeShares'] = ((target_portfolio['TargetValue'] - target_portfolio['Value'])
                                   / target_portfolio['lastPrice']).round(0)
# TODO tweak to ignore cash
target_portfolio['TradeDirection'] = np.where(target_portfolio['TradeShares'] > 0, 'BUY', 'SELL')

# Generate the trade blotter
post_trades.to_csv(target_portfolio)
