import yfinance as yf
# import pandas as pd
import streamlit as st

st.write("""
# Stock Price App

Shown are the stock closing price and volume of Google!
""")
# define the ticker symbol
tickerSymbol = 'GOOGL'
# get dat on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31',end='2020-5-31')


st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

# (what I use to run on PyCharm) streamlit run /Users/A3X/PycharmProjects/pythonPractice/Stock_Price.py [ARGUMENTS]
