import streamlit as st
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

def _get_title(ticker):
    df = get_tickers()
    tk = df[df['Symbol'].isin([ticker])]
    id = tk.index[0]
    name = tk['Name'][id]
    sector = tk['Sector'][id]
    industry = tk['Industry'][id]

    title= name + ' ({})</br>'.format(ticker)
    title += ' </br>Sector: {}'.format(sector)
    title += ', {}</br>'.format(industry)
    return title


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
        title= _get_title(ticker),
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

@st.cache
def get_tickers():
    path = r'static/nasdaq_screener_1631567663733.csv'
    return pd.read_csv(path)

def app():
    st.markdown("## Stock Price")
    df = get_tickers()
    tickers = df['Symbol'].drop_duplicates()

    ticker = st.sidebar.selectbox('Enter ticker ID!', tickers)
    if ticker:
        interval = st.sidebar.selectbox('Select interval', ['1m','5m','15m','1h','1d'], index=4)

        if interval:
            _view_chart(
                ticker=ticker,
                interval=interval
            )
        


    
