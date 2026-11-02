import yfinance as yf
import numpy as np

# NSE tickers end with .NS
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

# Download 2 years of daily closing prices
prices = yf.download(stocks, period="2y")["Close"]

# Show the first 5 rows to check the data loaded
print(prices.head())

# Daily return = (aaj ka price - kal ka price) / kal ka price
returns = prices.pct_change().dropna()

print(returns.head())

# Volatility = daily returns ka standard deviation
volatility = returns.std()
print("Daily volatility:")
print(volatility)

# Saal bhar ka number (finance mein yahi dikhate hain)
annual_volatility = volatility * np.sqrt(252)
print("Annual volatility:")
print(annual_volatility)

# 95% VaR = daily returns ka neeche wala 5th percentile
var_95 = returns.quantile(0.05)
print("95% VaR (daily):")
print(var_95)

# Max drawdown = biggest fall from a previous peak
cumulative = (1 + returns).cumprod()
running_max = cumulative.cummax()
drawdown = (cumulative - running_max) / running_max
max_drawdown = drawdown.min()
print("Max drawdown:")
print(max_drawdown)

# Correlation = how much the stocks move together
correlation = returns.corr()
print("Correlation:")
print(correlation)

import matplotlib.pyplot as plt

# Graph 1: stock prices
prices.plot(title="Stock Prices (2 years)", figsize=(10, 5))
plt.ylabel("Price (INR)")
plt.savefig("prices.png")
plt.show()

# Graph 2: annual volatility comparison
annual_volatility.plot(kind="bar", title="Annual Volatility", figsize=(6, 4))
plt.ylabel("Volatility")
plt.savefig("volatility.png")
plt.show()

# Graph 3: 95% VaR comparison
var_95.plot(kind="bar", title="95% Daily VaR", figsize=(6, 4), color="red")
plt.ylabel("Daily return")
plt.savefig("var.png")
plt.show()