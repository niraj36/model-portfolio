from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Investment(Base):
    __tablename__ = 'Investment'
    Id = Column(Integer, primary_key=True)
    Ticker = Column(String, nullable=False)
    Description = Column(String, nullable=False)

    def __repr__(self):
        return 'Id: {}, Ticker {}, Description {}'.format(self.Id, self.Ticker, self.Description)


class MarketDataType(Base):
    __tablename__ = 'MarketDataType'
    Id = Column(Integer, primary_key=True)
    Description = Column(String, nullable=False)

    def __repr__(self):
        return 'Id {}, Description {}'.format(self.Id, self.Description)


class MarketData (Base):
    __tablename__ = 'MarketData'
    Id = Column(Integer, primary_key=True)
    InvestmentId = Column(Integer, ForeignKey(Investment.Id), nullable=False)
    MarketDataTypeId = Column(Integer, ForeignKey(MarketDataType.Id), nullable=False)
    EffectiveDate = Column(DateTime, nullable=False)
    Value = Column(Float, nullable=False)
    Source = Column(String, nullable=False)
    CreateDate = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __repr__(self):
        return 'Id {}, InvestmentId {}, MarketDataTypeId {}, Value {}, Source {}, CreateDate{}'\
            .format(self.Id, self.InvestmentId, self.MarketDataTypeId, self.Value, self.Source, self.CreateDate)
