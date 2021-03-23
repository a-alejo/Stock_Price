import yfinance as yf
import streamlit as st

st.write("""
# Simple Historical Stock Data

Below are the stock closing price and volume of Apple!
""")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'AAPL'
# get dat on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
