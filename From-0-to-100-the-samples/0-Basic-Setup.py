from __future__ import (absolute_import, division, print_function,unicode_literals)
#让python2兼容python3，python3环境下可以不用写

#引入backtrader
import backtrader as bt

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    # cerebro.broker.setcash(100.0) #可以自定义金额

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())