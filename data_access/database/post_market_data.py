import pandas as pd
import os
from sqlalchemy import *
from sqlalchemy.orm import *
import datetime
from data_access.database import models


def from_yahoo_csv_adjusted_close(file):
    load_fields = ['Date', 'Adj Close']
    data = pd.read_csv(file, usecols=load_fields)
    ticker = os.path.splitext(os.path.basename(file))[0]
    market_data_type = 'Adjusted close'

    # create database connection
    engine = create_engine(open('C:/_data/DatabaseConnectionSting_ModelPortfolio.txt', 'r').read(), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    # check if market data type exists and add if missing
    if session.query(exists().where(models.MarketDataType.Description == market_data_type)).scalar() == False:
        new_market_data_type = models.MarketDataType(Description=market_data_type)
        session.add(new_market_data_type)
        session.commit()
        market_data_type_id = session.query(models.MarketDataType.Id).\
            filter(models.MarketDataType.Description == market_data_type).one()
    else:
        market_data_type_id = session.query(models.MarketDataType.Id).\
            filter(models.MarketDataType.Description == market_data_type).one()

    # check if investment exists and add if missing
    if session.query(exists().where(models.Investment.Ticker == ticker)).scalar() == False:
        new_investment = models.Investment(Ticker=ticker, Description=ticker)
        session.add(new_investment)
        session.commit()
        investment_id = session.query(models.Investment.Id).filter(models.Investment.Ticker == ticker).one()
    else:
        investment_id = session.query(models.Investment.Id).filter(models.Investment.Ticker == ticker).one()

    # prepare data for insert into the MarketData table
    data['InvestmentId'] = investment_id[0]
    data['MarketDataTypeId'] = market_data_type_id[0]
    data['Source'] = 'Yahoo!'
    data['CreateDate'] = datetime.datetime.utcnow()
    data.rename(columns={'Date': 'EffectiveDate'}, inplace=True)
    data.rename(columns={'Adj Close': 'Value'}, inplace=True)

    # insert market data
    data.to_sql('MarketData', engine, if_exists='append', index=false)
    return
