


import tushare as ts
import pandas as pd
import time



def _get_data(need_token = False):


    # 新接口，需要token
    tushare_token = "9897de9903a7ce04fa4b85bab5e531b6033d63e197faa87b7de5317f"

    if need_token:
        pro = ts.set_token(tushare_token)
        # pro = ts.pro_api(tushare_token)
        pro = ts.pro_api()

        current_day = time. strftime ( "%Y%m%d" )
        # df = pro.daily(ts_code='600036.SH', start_date='20190101', end_date='20210718')
        df = pro.daily(ts_code='600036.SH', start_date='20190101', end_date=current_day)
        # 修改列名
        df.rename(columns={'trade_date': 'date'}, inplace=True)

        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')
        df.index = df['date']
        df = df[
            ['ts_code', 'open', 'high', 'low', 'close', 'pre_close', 'change', 'pct_chg', 'vol', 'amount']]

        # print(df)
        df.to_csv('data/600036-3.csv')

    else:
        # 旧接口，不用token
        df = ts.get_hist_data('600036')
        # 直接保存
        df.to_csv('data/600036-1.csv')
        # 选择保存
        df.to_csv('data/600036-2.csv', columns=['open', 'high', 'low', 'close'])



def get_data():
    need_token = True
    _get_data(need_token)
    # get_data()

    # 获得股票池全部数据
    # for i in range(len(code)):
    #     data = ts_get_daily_stock(code.iloc[i], '20190101', '')  # 字段分别为股票代码、开始日期、结束日期
    #     data.to_csv(code.iloc[i] + '.csv')