import pandas_datareader as web
import numpy as np

class Portfolio:
    def __init__(self, balance, stocks, start, end):
        self.balance = balance
        self.tickers = stocks
        self.stock_data = web.get_data_yahoo(self.tickers, start, end)
        self.num_stocks = len(stocks)
        self.daily_returns = self.stock_data['Adj Close'].pct_change()
        self.mu = self.daily_returns.mean().to_numpy()[:,None]
        self.S = self.daily_returns.cov().to_numpy()

    def global_minimum_variance(self):
        np.set_printoptions(suppress=True)
        M = np.block([[2 * self.S, np.ones((self.num_stocks,1))], [np.ones((1,self.num_stocks)), np.zeros(1)]])
        soln = np.dot(np.linalg.inv(M), np.hstack([np.zeros(self.num_stocks), 1])[:,None])
        
        xbar = soln[0:self.num_stocks]
        risk = np.dot(np.dot(xbar.T, self.S), xbar)[0,0]
        ret = np.dot(xbar.T, self.mu)[0,0]
        portfolio = xbar * self.balance

        print(f"Risk: {risk}")
        print(f"Return: {ret}")
        print(f"Portfolio: \n{portfolio}")
        
        
