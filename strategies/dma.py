
'''
    双均线策略
'''

import backtrader as bt

class PrintClose(bt.Strategy):
    def __init__(self):
        ##引用data[0]中的收盘价格数据
        self.dataclose = self.datas[0].close

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt)) #Print date and close

    def next(self):
        #将收盘价保留两位小数再输出
        self.log('Close: %.2f' % self.dataclose[0])

