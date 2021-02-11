import pandas_datareader as web
import numpy as np

class Portfolio:
    def __init__(self, balance, stocks, start, end):
        self.balance = balance
        self.tickers = stocks
        self.stock_data = web.get_data_yahoo(self.tickers, start, end)
        self.daily_returns = self.stock_data['Adj Close'].pct_change()
        self.mu = self.daily_returns.mean().to_numpy().reshape((3,1))
        self.S = self.daily_returns.cov().to_numpy()

    def global_minimum_variance(self):
        print(self.mu)
        print(self.S)
        
