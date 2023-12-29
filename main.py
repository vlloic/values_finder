# add more components (russel, cac, euronext, etc..)
# https://github.com/ranaroussi/yfinance/tree/main
# KPI: trailingPE | debtToEquity | freeCashflow
# Need a bit of viz to understand distribution of the metrics --> easier to move to Jupyter?

import bs4 as bs
import requests
import yfinance as yf
import pandas as pd

resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})

tickers = []

for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker)

tickers = [s.replace('\n', '') for s in tickers]

sp_under_twelve = []

for i in tickers:
    stock_info = yf.Ticker(i)
    stock_dict = stock_info.info
    df = pd.DataFrame.from_dict(stock_dict, orient='index')
    df = df.reset_index()
    df = df.rename(columns={'index': 'info', 0: 'value'})
    if (df['value'][df['info'] == 'trailingPE'] < 12).any():
        sp_under_twelve.append(i)

print(sp_under_twelve)






