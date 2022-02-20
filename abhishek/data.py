import backtrader as bt
import pandas_datareader as web

class Data:
    def __init__():
        pass
    def get_data(ticker,start,end,*args,**kwargs):
        df = web.DataReader(ticker, 'yahoo', start=start, end=end,*args,**kwargs)
        return df
    
#df=Data.get_data("MSFT",start='2019-09-10', end='2019-10-09')



