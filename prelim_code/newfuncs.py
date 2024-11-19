import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import yfinance as yf

from statsmodels.regression.quantile_regression import QuantReg

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.linear_model import QuantileRegressor
from sklearn.decomposition import PCA

from scipy.optimize import lsq_linear

from datetime import datetime, timedelta


import warnings
warnings.filterwarnings("ignore")



def download_yf_data(tickers, start_date, end_date):
    """
    Downloads historical data from Yahoo Finance for a given list of tickers, start date, and end date.

    Parameters:
    tickers (list): List of stock ticker symbols.
    start_date (str): Start date in the format 'YYYY-MM-DD'.
    end_date (str): End date in the format 'YYYY-MM-DD'.

    Returns:
    dict: A dictionary with ticker symbols as keys and corresponding DataFrames as values.
    """
    data = {}
    for ticker in tickers:
        try:
            ticker_data = yf.download(ticker, start=start_date, end=end_date, progress= False)['Adj Close']
            data[ticker] = ticker_data
        except Exception as e:
            print(f"Failed to download data for {ticker}: {e}")
    return pd.DataFrame(data)


