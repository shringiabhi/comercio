# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:56:36 2022

@author: hp
"""
from datetime import datetime
import backtrader as bt
from matplotlib import pyplot as plt
from sgn_strategies import SmaCross,TestStrategy,DipStrategy
from data import Data
from alpaca_backtrader import data
#Specifying start and end
end = "2020-05-06"
start = "2020-05-04"

dataframe = data('GOOG',start,end)
#print(dataframe)
cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

# data0 = bt.feeds.YahooFinanceCSVData(dataname='data\oracle.csv', 
#                                     fromdate=datetime(2011, 1, 1),
#                                     todate=datetime(2012, 12, 31),reverse=False)
data0=bt.feeds.PandasData(dataname=dataframe)
cerebro.adddata(data0)





broker = cerebro.broker
broker.setcommission(commission=0.001)
broker.set_cash(1000000)
print("initial amount",cerebro.broker.getvalue())


cerebro.run()
print("final amount",cerebro.broker.getvalue())
cerebro.plot()

