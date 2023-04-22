import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App

Below is the stock **closing price** and **volume** of Tesla Stock

""")

# define the ticker symbol
tickerSymbol = 'TSLA'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical price data for the ticker
tickerDf = tickerData.history(period='1d', start='2010-01-01')

# use Open High Low Close Volume

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)