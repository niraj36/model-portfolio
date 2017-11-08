def equal_weight(marked_portfolio):
    target_value = marked_portfolio
    target_value['PortfolioValue'] = target_value['Value'].groupby(target_value['Portfolio']).transform('sum')
    target_value['PortfolioHoldingCount'] = target_value.groupby(target_value['Portfolio'])['Symbol'].transform('count')
    target_value['TargetValue'] = target_value['PortfolioValue'] / target_value['PortfolioHoldingCount']
    return target_value
