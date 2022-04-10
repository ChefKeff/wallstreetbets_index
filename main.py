from pathlib import Path
from pytrends.request import TrendReq
from pytrends import dailydata
import yfinance as yf
import pandas as pd
import os
dir_str_wsb = './wallstreetbets/'
dir_str_vals = './stockvals/'
dir_str_mod_wsb = './wsb_mod_percent/'
dir_str_google = './google_trends/'
date_and_stock_dict = {}
avg_dict = {}

pathlist = Path(dir_str_wsb).glob('**/*.csv')
pathlist_mod = Path(dir_str_mod_wsb).glob('**/*.csv')
pathlist_vals = Path(dir_str_vals).glob('**/*.csv')
pathlist_google = Path(dir_str_google).glob('**/*.csv')


def generate_tickers():
    already_collected = []
    for stock in pathlist_vals:
        print(str(str(stock)[10::].split('.')[0]))
        already_collected.append(str(str(stock)[10::].split('.')[0]))
    for path in pathlist:
        ticker = str(str(path)[15::].split('.')[0])
        if ticker not in already_collected:
            try:
                yfinance_data = yf.download(
                    ticker, start="2016-05-01", end="2022-01-01")
                if not yfinance_data.empty:
                    with open(f'./stockvals/{ticker}.csv', 'w') as fp:
                        yfinance_data.to_csv(fp)
            except:
                print("!ERROR!" + ticker)


# change so that it uses pytrends instead of yfinance

def get_over_800_mentions_wsb():
    vals = []
    over_800 = []
    for path in pathlist_vals:
        ticker_vals = str(str(path)[10::].split('.')[0])
        vals.append(ticker_vals)
    for path in pathlist:
        ticker = str(str(path)[15::].split('.')[0])
        if ticker in vals:
            df = pd.read_csv(path)
            if len(df) > 800:
                over_800.append(ticker)
    with open(f'./over_800_wsb_points.csv', 'w') as fp:
        pd.DataFrame(over_800).to_csv(fp)


def remove_empty_csvs():
    for path in pathlist_mod:
        df = pd.read_csv(path)
        if df.empty:
            print(path)
            os.remove(path)


pytrends = TrendReq(hl='en-US', tz=360)
# change so that it uses pytrends instead of yfinance


def get_google_trends():
    df = pd.read_csv('./over_800_wsb_points.csv')
    collected_tickers = []
    for path in pathlist_google:
        already_collected_ticker = str(
            str(path)[14::].split('.')[0]).split('_')[0]
        collected_tickers.append(already_collected_ticker)
    df.columns = ['index', 'Ticker']
    for ticker in df["Ticker"]:
        print(ticker)
        if ticker not in collected_tickers:
            google_trends_data = dailydata.get_daily_data(
                ticker, 2016, 5, 2021, 12, geo='US')
            with open(f'./google_trends/{ticker}_google_data.csv', 'w') as fp:
                google_trends_data.to_csv(fp)


def create_combo_gt_wsb_csv():
    for path in pathlist:
        df = pd.read_csv(path)
        df.columns = ['Date', 'Sentiment']
        df['Normalized_Sentiment'] = ((
            df.iloc[:, 1] - df.iloc[:, 1].min()) / (df.iloc[:, 1].max() - df.iloc[:, 1].min())) + 0.001
        df['Sentiment_Change_Percentual'] = df.iloc[:, 2].pct_change()
        Ticker = str(str(path)[15::].split('.')[0])
        df['Ticker'] = Ticker
        try:
            df2 = pd.read_csv(f'./stockvals/{Ticker}.csv')
            df3 = pd.read_csv(f'./google_trends/{Ticker}_google_data.csv')
            df3.columns = ["Date", f'{Ticker}_unscaled',
                           f'{Ticker}_monthly', 'isPartial', 'scale', Ticker]
            output1 = pd.merge(df, df2,
                               on='Date',
                               how='inner')
            try:
                output = pd.merge(output1, df3, on="Date", how="inner")
                output["Stock_Price_Change"] = output["High"].diff()
                output["Stock_Price_Change_Percent"] = output["High"].pct_change()
                with open(f'./preprocessed_stocks/{Ticker}_preprocess.csv', 'w') as fp:
                    output.to_csv(fp)
            except:
                print(Ticker, "was not in ./google_trends")
                pass
        except:
            print(Ticker, "was not in ./stockvals")
            pass


create_combo_gt_wsb_csv()
