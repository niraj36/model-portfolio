import pandas as pd


def from_sigfig():
    return_fields = ['Portfolio', 'Symbol', 'Shares']
    holdings = pd.read_csv('C:/_data/Portfolios.csv', usecols=return_fields)
    return holdings
