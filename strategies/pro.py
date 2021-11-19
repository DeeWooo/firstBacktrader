import backtrader as bt
import message as message
import datetime



'''双均线'''
class SmaCross(bt.Strategy):
    # 定义参数
    params = dict(
        fast_period=10,  # 快速移动平均期数
        slow_period = 60,)  # 慢速移动平均期数

    def __init__(self):
        # 定义快速移动平均线指标
        self.fastMA = bt.indicators.SMA(period=self.params.fast_period)

        # 定义慢速移动平均线指标
        self.slowMA = bt.indicators.SMA(period=self.params.slow_period)

        # 定义移动均线交叉信号指标
        self.crossover = bt.ind.CrossOver(self.fastMA, self.slowMA)

        self.order = None    # 设置订单引用，用于取消以往发出的尚未执行的订单


    def next(self): # 每个新bar结束时触发调用一次，相当于其他框架的 on_bar()方法

        self.cancel(self.order) # 取消以往未执行订单

        # if not self.position:  # 还没有仓位，才可以买
        #     if self.crossover > 0:  # 金叉
        #         # self.order = self.buy(size=100) # 创建市价买单，该单会在次日开盘以开盘价成交
        #         self.order = self.order_target_percent(target=0.8)
        #
        #
        # # 已有仓位，才可以卖
        # elif self.crossover < 0:  # 死叉
        #     # self.order = self.sell() # 创建市价卖单，该单会在次日开盘以开盘价成交
        #     self.order = self.order_target_value(target=0)

        # print(self.data0.datetime.date(0))
        # print(self.fastMA.get(), self.slowMA.get())
        trade_day = self.data0.datetime.date(0)
        cur_date = datetime.datetime.now().date()
        # cur_date = datetime.datetime(2021, 11, 16).date()

        pre_date = cur_date + datetime.timedelta(days=-1)

        # current_day
        if self.crossover < 0 and self.position:  # 死叉且有仓位
            self.order = self.order_target_value(target=0)
            # 提醒信息
            # print(trade_day)
            print(cur_date)
            # print(pre_date)
            if trade_day == pre_date:
                message.send_message("全部卖出")


        if self.crossover > 0 and not self.position: # 金叉且没有仓位
            self.order = self.order_target_percent(target=0.8)
            # 提醒信息
            # print(trade_day)
            print(cur_date)
            # print(pre_date)
            if trade_day == pre_date:
                message.send_message("全仓买入")


