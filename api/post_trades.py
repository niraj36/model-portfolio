def to_csv(target_portfolio):
    path = 'C:/_data/'
    blotter = target_portfolio[['Portfolio', 'Symbol', 'TradeShares', 'TradeDirection']].copy()
    blotter.to_csv(path_or_buf='C:/_data/TRADES.csv')
    print(blotter)
