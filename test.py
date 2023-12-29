
import yfinance as yf
import pandas as pd

tickers = ['AFL', 'ALB', 'MO', 'AAL', 'AIG', 'APA', 'APTV', \
        'ACGL', 'ADM', 'BAC', 'BWA', 'BG', 'COF', 'CE', 'CF', \
        'CVX', 'CINF', 'C', 'CFG', 'CMA', 'CTRA', 'DE', 'DAL', 'DVN', \
        'FANG', 'DFS', 'DHI', 'EBAY', 'EOG', 'EQT', 'EG', 'XOM', 'FITB',\
        'F', 'GEN', 'GM', 'HIG', 'HPE', 'HPQ', 'HBAN', 'JPM', 'KEY', 'LEN', \
        'L', 'MTB', 'MRO', 'MPC', 'MOS', 'NUE', 'PSX', 'PXD', 'PNC', 'PEG', 'PHM', \
        'RF', 'STT', 'STLD', 'SYF', 'TPR', 'TFC', 'UAL', 'VLO', 'VZ', 'VTRS', 'WFC', 'ZION']

test = []

for i in tickers:
    stock_info = yf.Ticker(i)  # Corrected this line to use the ticker 'i' instead of the string 'i'
    stock_dict = stock_info.info
    df = pd.DataFrame.from_dict(stock_dict, orient='index')
    df = df.reset_index()
    df = df.rename(columns={'index': 'info', 0: 'value'})
    if (df[df['info']=='freeCashflow']['value'] > 0).any():  # Corrected this line to use ['value']
        test.append(i)

print(test)  # Corrected this line to print the list 'test' instead of the individual ticker 'i'

cashflow_above_zero = ['MO', 'AAL', 'AIG', 'APA', 'APTV', 'ACGL', 'ADM',\
                       'BWA', 'BG', 'CF', 'CVX', 'CINF', 'CTRA', 'DE', 'DAL', \
                       'DVN', 'DHI', 'EBAY', 'EOG', 'EQT', 'EG', 'XOM', 'GEN',\
                       'GM', 'HIG', 'HPE', 'HPQ', 'L', 'MRO', 'MPC', 'MOS', 'NUE', \
                       'PSX', 'PXD', 'PEG', 'PHM', 'STLD', 'TPR', 'VLO', 'VZ', 'VTRS']
