import yfinance as yf

def get_data(ticker, period, interval):
    return yf.download(ticker, period=period, interval=interval)
