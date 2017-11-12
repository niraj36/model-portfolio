# Saves trade blotter to file and prints
def to_csv(target_portfolio):
    blotter = target_portfolio[['Portfolio', 'Symbol', 'TradeDirection', 'TradeShares', 'lastPrice']].copy()
    blotter.to_csv(path_or_buf='C:/_data/TRADES.csv')
    print(blotter)
