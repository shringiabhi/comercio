from alpaca_trade_api.rest import REST, TimeFrame
from local_settings import alpaca_paper
api_key = alpaca_paper['api_key']
api_secret = alpaca_paper['api_secret']
base_url = alpaca_paper['end_point']
api = REST(api_key, api_secret, base_url, api_version='v2')

def data(ticker,fromdate,todate):
    df=api.get_bars(ticker, TimeFrame.Hour, fromdate, todate, adjustment='raw').df
    return df
#print(df.columns)


# import alpaca_backtrader_api as Alpaca
# import backtrader as bt
# import pytz
# from datetime import datetime
# from local_settings import alpaca_paper

# ALPACA_KEY_ID = alpaca_paper['api_key']
# ALPACA_SECRET_KEY = alpaca_paper['api_secret']
# ALPACA_PAPER = True

# fromdate = datetime(2011,8,6)
# todate = datetime(2011,8,15)

# tickers = ['SPY']
# timeframes = {
#     '15Min':15,
#     '30Min':30,
#     '1H':60,
# }


# class RSIStack(bt.Strategy):
#     def __init__(self):
#         pass
#     def next(self):
#         print(len(self.datas))
#         # for i in range(0,len(self.datas)):
#         #     print(f'{self.datas[i].datetime.datetime(ago=0)} \
#         #     {self.datas[i].p.dataname}: OHLC: \
#         #         o:{self.datas[i].open[0]} \
#         #         h:{self.datas[i].high[0]} \
#         #         l:{self.datas[i].low[0]} \
#         #         c:{self.datas[i].close[0]} \
#         #         v:{self.datas[i].volume[0]}' )

# cerebro = bt.Cerebro()
# cerebro.addstrategy(RSIStack)
# cerebro.broker.setcash(100000)
# cerebro.broker.setcommission(commission=0.0)

# store = Alpaca.AlpacaStore(
#     key_id=ALPACA_KEY_ID,
#     secret_key=ALPACA_SECRET_KEY,
#     paper=ALPACA_PAPER
# )

# if not ALPACA_PAPER:
#     print(f"LIVE TRADING")
#     broker = store.getbroker()
#     cerebro.setbroker(broker)

# DataFactory = store.getdata

# for ticker in tickers:
#     for timeframe, minutes in timeframes.items():
#         print(f'Adding ticker {ticker} using {timeframe} timeframe at {minutes} minutes.')

#         d = DataFactory(
#             dataname=ticker,
#             timeframe=bt.TimeFrame.Minutes,
#             compression=minutes,
#             fromdate=fromdate,
#             todate=todate,
#             historical=True)

#         cerebro.adddata(d)

# cerebro.run()
# print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())
#cerebro.plot(style='candlestick', barup='green', bardown='red')
######################################################################
# import alpaca_backtrader_api
# import backtrader as bt
# from datetime import datetime
# from local_settings import alpaca_paper
# ###################################################################
# ALPACA_API_KEY = alpaca_paper['api_key']
# ALPACA_SECRET_KEY = alpaca_paper['api_secret']
# ALPACA_PAPER = True
# #################################################################
# class SmaCross(bt.SignalStrategy):
#   def __init__(self):
#     sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
#     crossover = bt.ind.CrossOver(sma1, sma2)
#     self.signal_add(bt.SIGNAL_LONG, crossover)
# ###############################################################

# cerebro = bt.Cerebro()
# cerebro.addstrategy(SmaCross)

# store = alpaca_backtrader_api.AlpacaStore(
#     key_id=ALPACA_API_KEY,
#     secret_key=ALPACA_SECRET_KEY,
#     paper=ALPACA_PAPER
# )

# if not ALPACA_PAPER:
#   broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
#   cerebro.setbroker(broker)

# DataFactory = store.getdata  # or use alpaca_backtrader_api.AlpacaData
# data0 = DataFactory(dataname='AAPL', historical=True, fromdate=datetime(2015, 1, 1), timeframe=bt.TimeFrame.Days)
# cerebro.adddata(data0)

# print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
# cerebro.run()
# print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot()
