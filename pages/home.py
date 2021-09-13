import streamlit as st
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

def _view_chart(ticker, interval):
    period = '30d'
    if interval == '1m':
        period = '7d'
    data = yf.download(tickers=ticker, period=period, interval=interval)
    #declare figure
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(
        title='Uber live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    st.plotly_chart(fig)

def app():
    st.markdown("## Home Page")

    ticker = st.sidebar.text_input('Enter ticker ID!')
    if ticker:
        interval = st.sidebar.selectbox('Select interval', ['1m','5m','15m','1h','1d'])

        if interval:
            _view_chart(
                ticker=ticker,
                interval=interval
            )
        


    
