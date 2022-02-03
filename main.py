from pathlib import Path
from pytrends.request import TrendReq
import yfinance as yf
import pandas as pd
import json
import time
from datetime import date, timedelta
dir_str = './wallstreetbets/'
date_and_stock_dict = {}
avg_dict = {}

pathlist = Path(dir_str).glob('**/*.csv')


def create_dict(date_and_stock_dict):
    for path in pathlist:
        stock = pd.read_csv(f"./{path}")
        for index in range(len(stock.iloc[:, 0])):
            if stock.iloc[:, 0][index] not in date_and_stock_dict:
                date_and_stock_dict[str(stock.iloc[:, 0][index])
                                    ] = [[str(str(path)[15::].split('.')[0]), int(stock.iloc[:, 1][index])]]
            else:
                date_and_stock_dict[str(stock.iloc[:, 0][index])
                                    ] += [[str(str(path)[15::].split('.')[0]), int(stock.iloc[:, 1][index])]]

    with open('date_and_stock.json', 'w') as fp:
        json.dump(date_and_stock_dict, fp)


def generate_avg_dict(avg_dict):
    f = open('date_and_stock.json')
    data_dict = json.load(f)
    for datestr in data_dict:
        avg_val = 0
        denom = 0
        for stonk in data_dict[datestr]:
            t = time.strptime(str(datestr), '%Y-%m-%d')
            newdate = date(t.tm_year, t.tm_mon, t.tm_mday)+timedelta(1)
            yfinance_data = yf.download(
                stonk[0], start=datestr, end=newdate)
            avg_val += (yfinance_data['Open'] + yfinance_data['High'] +
                        yfinance_data['Low'] + yfinance_data['Close'] + yfinance_data['Adj Close']) / 5
            denom += 1

        avg_dict[datestr] = {
            'avg_price': avg_val / denom
        }
        with open('avg.json', 'w') as fp:
            json.dump(avg_dict, fp)


generate_avg_dict(avg_dict)
