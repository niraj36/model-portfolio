# Equal weight portfolio in case no clear over/under wight asset allocation signal exists
def equal_weight(marked_portfolio):
    target_value = marked_portfolio

    # Calculate the total value of holdings by portfolio
    target_value['PortfolioValue'] = target_value['Value'].groupby(target_value['Portfolio']).transform('sum')

    # Calculate the number of non cash holdings by portfolio
    target_value['PortfolioHoldingCount'] = target_value.groupby(target_value['Portfolio'])['symbol'].transform('count')

    # Calculate the target market value of each holding within the portfolio
    target_value['TargetValue'] = target_value['PortfolioValue'] / target_value['PortfolioHoldingCount']
    return target_value
