from pathlib import Path
from pytrends.request import TrendReq
import yfinance as yf
import pandas as pd
import os
dir_str_wsb = './wallstreetbets/'
dir_str_vals = './stockvals/'
dir_str_mod_wsb = './wsb_mod_percent/'
date_and_stock_dict = {}
avg_dict = {}

pathlist = Path(dir_str_wsb).glob('**/*.csv')
pathlist_mod = Path(dir_str_mod_wsb).glob('**/*.csv')
pathlist_vals = Path(dir_str_vals).glob('**/*.csv')

# create_dict function is not currently used
# I think the stock .csv-files will be sufficient in doing the analysis in rapidminer
# def create_dict(date_and_stock_dict):
#     for path in pathlist:
#         stock = pd.read_csv(f"./{path}")
#         for index in range(len(stock.iloc[:, 0])):
#             if stock.iloc[:, 0][index] not in date_and_stock_dict:
#                 date_and_stock_dict[str(stock.iloc[:, 0][index])
#                                     ] = [[str(str(path)[15::].split('.')[0]), int(stock.iloc[:, 1][index])]]
#             else:
#                 date_and_stock_dict[str(stock.iloc[:, 0][index])
#                                     ] += [[str(str(path)[15::].split('.')[0]), int(stock.iloc[:, 1][index])]]

#     with open('date_and_stock.json', 'w') as fp:
#         json.dump(date_and_stock_dict, fp)

# generate_tickers generates a .json-file for each stock with all the values bw 2016-05-01 & 2022-01-01
handled_tickers_yfinance = []
print(handled_tickers_yfinance)


def generate_tickers():
    i = 0
    for path in pathlist:
        ticker = str(str(path)[15::].split('.')[0])
        if ticker not in handled_tickers_yfinance:
            yfinance_data = yf.download(
                ticker, start="2016-05-01", end="2022-01-01")
            if not yfinance_data.empty:
                with open(f'./stockvals/{ticker}.csv', 'w') as fp:
                    yfinance_data.to_csv(fp)
                    handled_tickers_yfinance.append(ticker)


# generate_tickers()


# change so that it uses pytrends instead of yfinance

def create_big_csvs():
    csvs = []
    for path in pathlist_vals:
        smalldf = pd.read_csv(path)
        smalldf.insert(1, "Ticker", str(str(path)[10::].split('.')[0]))
        csvs.append(smalldf)
    df = pd.concat(csvs, ignore_index=True)
    with open('output_yfinance_data.csv', 'w') as fp:
        df.to_csv(fp)


def create_mod_csv_wsb():
    for path in pathlist:
        fout = open("output_wsb_data.csv", "a")
        # first file:
        for line in open(path):
            df = pd.read_csv(path)
            df[3] = (
                df.iloc[:, 1] - df.iloc[:, 1].min()) / (df.iloc[:, 1].max() - df.iloc[:, 1].min())
            Ticker = str(str(path)[15::].split('.')[0])
            df[4] = Ticker
            with open(f'./wsb_mod/{Ticker}_mod.csv', 'w') as fp:
                df.to_csv(fp)


def create_mod_percent_csv_wsb():
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
            output = pd.merge(df, df2,
                              on='Date',
                              how='inner')
            output["Stock_Price_Change"] = output["High"].diff()
            output["Stock_Price_Change_Percent"] = output["High"].pct_change()
            with open(f'./wsb_mod_percent/{Ticker}_percent.csv', 'w') as fp:
                output.to_csv(fp)
        except:
            print(Ticker, "was not in ./stockvals")
            pass


def remove_empty_csvs():
    for path in pathlist_mod:
        df = pd.read_csv(path)
        if df.empty:
            print(path)
            os.remove(path)


def create_big_csv_wsb():
    for path in pathlist_mod:
        fout = open("output_wsb_data_percent.csv", "a")
        # first file:
        for line in open(path):
            fout.write(line)


def split_large_csv():
    df = pd.read_csv('./rapidminerTest/testBigStonk9.csv')
    print(df[4])


# change so that it uses pytrends instead of yfinance
def get_google_trends():
    for path in pathlist:
        ticker = str(str(path)[15::].split('.')[0])
        yfinance_data = yf.download(
            ticker, start="2016-05-01", end="2022-01-01")
        if not yfinance_data.empty:
            with open(f'./stockvals/{ticker}.json', 'w') as fp:
                yfinance_data.to_json(fp)


remove_empty_csvs()
