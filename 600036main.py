'''
backtrader主脚本
'''

import datetime

import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

import backtrader as bt
import pandas as pd

from backtrader_plotting import Bokeh, OptBrowser
from backtrader_plotting.schemes import Tradimo

from strategies import dev  as stg_dev
from strategies import pro  as stg
import dataprocess as dp

if __name__ == '__main__':


    dp.get_data()

    cerebro = bt.Cerebro()

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'data/600036.csv')

    dataframe = pd.read_csv(datapath, index_col=0, parse_dates=True)


    # Create a Data Feed,reverse 代表是否反转数据
    # data = bt.feeds.YahooFinanceCSVData(
    # data = bt.feeds.PandasData(
    #     dataname=dataframe,
    #     # Do not pass values before this date
    #     fromdate=datetime.datetime(2020, 1, 1),
    #     # Do not pass values after this date
    #     todate=datetime.datetime(2021, 10, 31))

    cur = datetime.datetime.now()
    # cur.hour
    # cur.minute
    # cur.year
    # cur.day
    # cur.month
    data = bt.feeds.GenericCSVData(
        dataname= 'data/600036.csv',
        fromdate=datetime.datetime(2019, 7, 1),
        todate=datetime.datetime(cur.year, cur.month, cur.day),
        dtformat='%Y-%m-%d',
        datetime=0,  # 定义trade_date在第0列
        open=2,
        high=3,
        low=4,
        close=5,
        volume=9,
        nullvalue=0.0,  # 设置空值
    )


        # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)

    # 改变账户初始金额
    cerebro.broker.set_cash(100000.0)

    # Set the commission - 0.1% ... divide by 100 to remove the % 交易佣金设置
    cerebro.broker.setcommission(commission=0.001)
    # 设置每笔交易交易的股票数量
    # cerebro.addsizer(bt.sizers.FixedSize, stake=100)

    # Add a strategy
    cerebro.addstrategy(stg.SmaCross)
    # cerebro.optstrategy(TestStrategy, maperiod=range(10, 31))


    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # cerebro.run()


    result = cerebro.run(optreturn=True)


    # 画图
    # cerebro.plot(style = 'candle')
    # cerebro.plot()

    b = Bokeh(style='bar', plot_mode='single', scheme=Tradimo())
    cerebro.plot(b)


    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
