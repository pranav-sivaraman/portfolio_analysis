from portfolio import Portfolio

print("Welcome to Doge Portfolio Optimization")
balance = input("Enter amount to invest: ")
stocks = input("Enter stock symbols: ")
start = input("Enter start date: ")
end = input("Enter end date: ")

stocks = [x.strip() for x in stocks.split(',')]
portfolio = Portfolio(balance, stocks, start, end)
portfolio.global_minimum_variance()