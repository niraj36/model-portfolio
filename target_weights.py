import pandas as pd


def equal_weight(marked_portfolio):
    # TODO calculate the total value of all etf holdings by portfolio
    portfolio_value = pd.DataFrame(marked_portfolio)
    # TODO calculate the number of etf holdings by portfolio
    position_count = 10
    # TODO calculate the expected value of each holding by portfolio if equal weighted
    target_value = marked_portfolio['Value'] * 100
    # TODO return the target values of each holding by portfolio
    return target_value
