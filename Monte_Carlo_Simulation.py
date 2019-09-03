import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from scipy.stats import norm

ticker = ['GOOG','FB', 'AMZN', 'NFLX', 'AAPL']
data = pd.DataFrame()
for item in ticker:
    data[item] = web.DataReader(item, data_source='yahoo', start='12-31-2013')['Adj Close']


returns = data.pct_change().dropna()

facebook = returns['FB']
apple = returns['AAPL']
amazon = returns['AMZN']
netflix = returns['NFLX']
google = returns['GOOG']

# Monte Carlo Simulation Function

def monte_carlo(ticker):
    mu, sigma = norm.fit(returns[ticker])
    paths = []
    for i in range(10):
        prc = [data[ticker].iloc[-1]]

        new_returns = np.random.normal(loc=mu, scale = sigma, size = 1000)

        for i in range(1,1000):
            prc.append(prc[i-1] * (1+new_returns[i]))
        paths.append(prc)

    for path in paths:
        plt.plot(path)
    plt.xlabel('Days')
    plt.ylabel('Stock Price')
    plt.suptitle(ticker)
    plt.show()

monte_carlo('AAPL')
