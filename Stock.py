# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:30:57 2021

@author: User
"""

import streamlit as st
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
st.write("""
          # STOCK PRICE APP
          """)

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start='2020-1-31', end='2021-1-31')

st.write('''
         # *Opening Price*
         ''')
st.line_chart(tickerDF.Open,use_container_width=True)
st.line_chart(tickerDF.Open)


st.write('''
         # *Closing Price*
         ''')
st.line_chart(tickerDF.Close)

st.write('''
         # *Volume Price*
         ''')
st.line_chart(tickerDF.Volume)