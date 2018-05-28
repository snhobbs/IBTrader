import os
from datetime import datetime as dt
import pandas as pd
import numpy as np
import pickle
import requests
import pandas_datareader as web
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import dates as mdates 

style.use('ggplot')

class StockAnalizer(object):
    def __init__(self, ticker):
        self.ticker = ticker
        self.dataSource = 'iex'

    def getTicker(self, start, end=dt.now()):
        df = web.DataReader(self.ticker, self.dataSource, start, end)
        return df

    def plot(self, df):
        df.plot(y="close",x=mdates(df.index), title=self.ticker.upper(), use_index = True)
        plt.xticks()

if __name__ == "__main__":
    sa = StockAnalizer('AAPL')
    start = dt(2015,1,1)
    df = sa.getTicker(start)
    df[['open']].plot()
    plt.show()
