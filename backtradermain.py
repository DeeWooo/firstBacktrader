import pandas as pd
import numpy as np
import backtrader as bt
import datetime


class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' log信息的功能'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 一般用于计算指标或者预先加载数据，定义变量使用
        pass

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log(f"招商银行,{self.datas[0].datetime.date(0)},收盘价为：{self.datas[0].close[0]}")


# 添加cerebro
cerebro = bt.Cerebro()
# 添加策略
cerebro.addstrategy(TestStrategy)
# 准备数据
params = dict(
    fromdate=datetime.datetime(2021, 10, 27),
    todate=datetime.datetime(2021, 11, 2),
    timeframe=bt.TimeFrame.Days,
    compression=1,
    # dtformat=('%Y-%m-%d %H:%M:%S'),
    # tmformat=('%H:%M:%S'),
    datetime=0,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=5,
    openinterest=6)

data_path = 'data/600036.csv'
df = pd.read_csv(data_path, encoding='gbk')
df = df[['日期', '开盘价', '最高价', '最低价', '收盘价', '成交量', '成交金额']]
df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'openinterest']
df = df.sort_values("datetime")
df.index = pd.to_datetime(df['datetime'])
df = df[['open', 'high', 'low', 'close', 'volume', 'openinterest']]
feed = bt.feeds.PandasDirectData(dataname=df, **params)
# 添加合约数据
cerebro.adddata(feed, name="gsyh")
cerebro.broker.setcommission(commission=0.0005)

# 添加资金
cerebro.broker.setcash(100000.0)

# 开始运行
cerebro.run()