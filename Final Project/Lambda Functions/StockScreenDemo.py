# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:45:01 2021

@author: Teo Bee Guan
"""

import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import bs4 
import requests
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pandas import DataFrame
import time
import nltk
import plotly.express as px

# Import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt

# NLTK VADER for sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

snp500 = pd.read_csv("Datasets/SP500.csv")
symbols = snp500['Symbol'].sort_values().tolist()        

ticker = st.sidebar.selectbox(
    'Choose a S&P 500 Stock',
     symbols)

infoType = st.sidebar.radio(
        "Choose an info type",
        ('Fundamental', 'Technical', 'Latest News', 'FizViz News')
    )

stock = yf.Ticker(ticker)

if(infoType == 'Fundamental'):
    stock = yf.Ticker(ticker)
    info = stock.info 
    st.title('Company Profile')
    st.subheader(info['longName']) 
    st.markdown('** Sector **: ' + info['sector'])
    st.markdown('** Industry **: ' + info['industry'])
    st.markdown('** Phone **: ' + info['phone'])
    st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
    st.markdown('** Website **: ' + info['website'])
    st.markdown('** Business Summary **')
    st.info(info['longBusinessSummary'])
        
    fundInfo = {
            'Enterprise Value (USD)': info['enterpriseValue'],
            'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
            'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
            'Net Income (USD)': info['netIncomeToCommon'],
            'Profit Margin Ratio': info['profitMargins'],
            'Forward PE Ratio': info['forwardPE'],
            'PEG Ratio': info['pegRatio'],
            'Price to Book Ratio': info['priceToBook'],
            'Forward EPS (USD)': info['forwardEps'],
            'Beta ': info['beta'],
            'Book Value (USD)': info['bookValue'],
            'Dividend Rate (%)': info['dividendRate'], 
            'Dividend Yield (%)': info['dividendYield'],
            'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
            'Payout Ratio': info['payoutRatio']
        }
    
    fundDF = pd.DataFrame.from_dict(fundInfo, orient='index')
    fundDF = fundDF.rename(columns={0: 'Value'})
    st.subheader('Fundamental Info') 
    st.table(fundDF)
    
    st.subheader('General Stock Info') 
    st.markdown('** Market **: ' + info['market'])
    st.markdown('** Exchange **: ' + info['exchange'])
    st.markdown('** Quote Type **: ' + info['quoteType'])
    
    start = dt.datetime.today()-dt.timedelta(2 * 365)
    end = dt.datetime.today()
    df = yf.download(ticker,start,end)
    df = df.reset_index()
    fig = go.Figure(
            data=go.Scatter(x=df['Date'], y=df['Adj Close'])
        )
    fig.update_layout(
        title={
            'text': "Stock Prices Over Past Two Years",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)
    
    marketInfo = {
            "Volume": info['volume'],
            "Average Volume": info['averageVolume'],
            "Market Cap": info["marketCap"],
            "Float Shares": info['floatShares'],
            "Regular Market Price (USD)": info['regularMarketPrice'],
            'Bid Size': info['bidSize'],
            'Ask Size': info['askSize'],
            "Share Short": info['sharesShort'],
            'Short Ratio': info['shortRatio'],
            'Share Outstanding': info['sharesOutstanding']
    
        }
    
    marketDF = pd.DataFrame(data=marketInfo, index=[0])
    st.table(marketDF)

elif(infoType == 'Latest News'):

    st.header('Latest News') 

    user_input = st.text_input("Please Enter a Company Name")

    
    def findnews(temp):
        
        # Adding a Sleep Time to avoid contant requests
        time.sleep(5)
        
        # Defining the Yahoo Link to Scrape News, Site and Time
        source = requests.get('https://ca.news.search.yahoo.com/search;_ylt=AwrJ7JKUXLxe4hIA6iTrFAx.;_ylu=X3oDMTB0N2Noc21lBGNvbG8DYmYxBHBvcwMxBHZ0aWQDBHNlYwNwaXZz?p='+temp+'&fr2=piv-web&fr=uh3_news_web_gs').text
        soup = bs4.BeautifulSoup(source, 'lxml')

        title_list = []
        site_list = []
        time_list = []

        try:
            for article in soup.find_all('div', class_="dd NewsArticle"):

                title_list.append(str(article.ul.li.a['title']))

                site_list.append(str(article.find('span', class_="s-source mr-5 cite-co").text))

                time_list.append(str(article.find('span', class_="fc-2nd s-time mr-8").text))
        except:
            
            finaldf = pd.DataFrame(
                {'Title': title_list,
                'Site': site_list,
                'Time': time_list},
            columns=['Title','Site', 'Time'])
            
        return pd.DataFrame(
                {'Title': title_list,
                'Site': site_list,
                'Time': time_list},
            columns=['Title','Site', 'Time'])


    # Find News Function

    def findnewssentiment(temp):
        
        df = findnews(temp)
        # Instantiate the sentiment intensity analyzer
        vader = SentimentIntensityAnalyzer()

        # Set column names
        columns = ['Title', 'Site', 'Time']

        # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
        parsed_and_scored_news = pd.DataFrame(df, columns=columns)

        # Iterate through the headlines and get the polarity scores using vader
        scores = parsed_and_scored_news['Title'].apply(vader.polarity_scores).tolist()

        # Convert the 'scores' list of dicts into a DataFrame
        scores_df = pd.DataFrame(scores)

        # Join the DataFrames of the news and the list of dicts
        parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix='_right')

        parsed_and_scored_news['Sentiment'] = np.where(parsed_and_scored_news['compound'] > 0, 'Positive', (np.where(parsed_and_scored_news['compound'] == 0, 'Neutral', 'Negative')))

        return parsed_and_scored_news

    if user_input == "":
        st.text('Please Enter a Valid Input')
    else:
        try:

            df = findnewssentiment(user_input)

            df_pie = df[['Sentiment','Title']].groupby('Sentiment').count()
            fig = px.pie(df_pie, values=df_pie['Title'], names=df_pie.index, color=df_pie.index, color_discrete_map={'Positive':'green', 'Neutral':'darkblue', 'Negative':'red'})

            st.header('Dataframe with Latest News')
            st.dataframe(df)

            st.header('Latest News Sentiment Distribution') 
            st.plotly_chart(fig)

            
        except:
            st.text('Please Enter a Valid Input')

    
elif(infoType == 'FizViz News'):

    st.header('Latest News') 

    st.header(ticker)

    def newsfromfizviz(temp):

        # time.sleep(5)

        finwiz_url = 'https://finviz.com/quote.ashx?t='


        news_tables = {}
        tickers = [temp]

        for ticker in tickers:
            url = finwiz_url + ticker
            req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
            response = urlopen(req)    
            # Read the contents of the file into 'html'
            html = BeautifulSoup(response)
            # Find 'news-table' in the Soup and load it into 'news_table'
            news_table = html.find(id='news-table')
            # Add the table to our dictionary
            news_tables[ticker] = news_table

        parsed_news = []

        # Iterate through the news
        for file_name, news_table in news_tables.items():
            # Iterate through all tr tags in 'news_table'
            for x in news_table.findAll('tr'):
                # read the text from each tr tag into text
                # get text from a only
                text = x.a.get_text() 
                # splite text in the td tag into a list 
                date_scrape = x.td.text.split()
                # if the length of 'date_scrape' is 1, load 'time' as the only element

                if len(date_scrape) == 1:
                    time = date_scrape[0]

                # else load 'date' as the 1st element and 'time' as the second    
                else:
                    date = date_scrape[0]
                    time = date_scrape[1]
                # Extract the ticker from the file name, get the string up to the 1st '_'  
                ticker = file_name.split('_')[0]

                # Append ticker, date, time and headline as a list to the 'parsed_news' list
                parsed_news.append([ticker, date, time, text])

        


        # Instantiate the sentiment intensity analyzer
        vader = SentimentIntensityAnalyzer()

        # Set column names
        columns = ['ticker', 'date', 'time', 'headline']

        # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
        parsed_and_scored_news = pd.DataFrame(parsed_news, columns=columns)

        # Iterate through the headlines and get the polarity scores using vader
        scores = parsed_and_scored_news['headline'].apply(vader.polarity_scores).tolist()

        # Convert the 'scores' list of dicts into a DataFrame
        scores_df = pd.DataFrame(scores)

        # Join the DataFrames of the news and the list of dicts
        parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix='_right')

        # Convert the date column from string to datetime
        parsed_and_scored_news['date'] = pd.to_datetime(parsed_and_scored_news.date).dt.date
        
        parsed_and_scored_news['Sentiment'] = np.where(parsed_and_scored_news['compound'] > 0, 'Positive', (np.where(parsed_and_scored_news['compound'] == 0, 'Neutral', 'Negative')))

        return parsed_and_scored_news

    df = newsfromfizviz(ticker)
    df_pie = df[['Sentiment','headline']].groupby('Sentiment').count()
    fig = px.pie(df_pie, values=df_pie['headline'], names=df_pie.index, color=df_pie.index, color_discrete_map={'Positive':'green', 'Neutral':'darkblue', 'Negative':'red'})

    st.header('Dataframe with Latest News')
    st.dataframe(df)

    st.header('Latest News Sentiment Distribution') 
    st.plotly_chart(fig)

    plt.rcParams['figure.figsize'] = [11, 5]

    # Group by date and ticker columns from scored_news and calculate the mean
    mean_scores = df.groupby(['ticker','date']).mean()

    # Unstack the column ticker
    mean_scores = mean_scores.unstack()

    # Get the cross-section of compound in the 'columns' axis
    mean_scores = mean_scores.xs('compound', axis="columns").transpose()

    # Plot a bar chart with pandas
    mean_scores.plot(kind = 'bar')

    plt.grid()

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()
    
    




else:
    def calcMovingAverage(data, size):
        df = data.copy()
        df['sma'] = df['Adj Close'].rolling(size).mean()
        df['ema'] = df['Adj Close'].ewm(span=size, min_periods=size).mean()
        df.dropna(inplace=True)
        return df
    
    def calc_macd(data):
        df = data.copy()
        df['ema12'] = df['Adj Close'].ewm(span=12, min_periods=12).mean()
        df['ema26'] = df['Adj Close'].ewm(span=26, min_periods=26).mean()
        df['macd'] = df['ema12'] - df['ema26']
        df['signal'] = df['macd'].ewm(span=9, min_periods=9).mean()
        df.dropna(inplace=True)
        return df

    def calcBollinger(data, size):
        df = data.copy()
        df["sma"] = df['Adj Close'].rolling(size).mean()
        df["bolu"] = df["sma"] + 2*df['Adj Close'].rolling(size).std(ddof=0) 
        df["bold"] = df["sma"] - 2*df['Adj Close'].rolling(size).std(ddof=0) 
        df["width"] = df["bolu"] - df["bold"]
        df.dropna(inplace=True)
        return df

    st.title('Technical Indicators')
    st.subheader('Moving Average')
    
    coMA1, coMA2 = st.beta_columns(2)
    
    with coMA1:
        numYearMA = st.number_input('Insert period (Year): ', min_value=1, max_value=10, value=2, key=0)    
    
    with coMA2:
        windowSizeMA = st.number_input('Window Size (Day): ', min_value=5, max_value=500, value=20, key=1)  
        

    start = dt.datetime.today()-dt.timedelta(numYearMA * 365)
    end = dt.datetime.today()
    dataMA = yf.download(ticker,start,end)
    df_ma = calcMovingAverage(dataMA, windowSizeMA)
    df_ma = df_ma.reset_index()
        
    figMA = go.Figure()
    
    figMA.add_trace(
            go.Scatter(
                    x = df_ma['Date'],
                    y = df_ma['Adj Close'],
                    name = "Prices Over Last " + str(numYearMA) + " Year(s)"
                )
        )
    
    figMA.add_trace(
                go.Scatter(
                        x = df_ma['Date'],
                        y = df_ma['sma'],
                        name = "SMA" + str(windowSizeMA) + " Over Last " + str(numYearMA) + " Year(s)"
                    )
            )
    
    figMA.add_trace(
                go.Scatter(
                        x = df_ma['Date'],
                        y = df_ma['ema'],
                        name = "EMA" + str(windowSizeMA) + " Over Last " + str(numYearMA) + " Year(s)"
                    )
            )
    
    figMA.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    
    figMA.update_layout(legend_title_text='Trend')
    figMA.update_yaxes(tickprefix="$")
    
    st.plotly_chart(figMA, use_container_width=True)  
    
    st.subheader('Moving Average Convergence Divergence (MACD)')
    numYearMACD = st.number_input('Insert period (Year): ', min_value=1, max_value=10, value=2, key=2) 
    
    startMACD = dt.datetime.today()-dt.timedelta(numYearMACD * 365)
    endMACD = dt.datetime.today()
    dataMACD = yf.download(ticker,startMACD,endMACD)
    df_macd = calc_macd(dataMACD)
    df_macd = df_macd.reset_index()
    
    figMACD = make_subplots(rows=2, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.01)
    
    figMACD.add_trace(
            go.Scatter(
                    x = df_macd['Date'],
                    y = df_macd['Adj Close'],
                    name = "Prices Over Last " + str(numYearMACD) + " Year(s)"
                ),
            row=1, col=1
        )
    
    figMACD.add_trace(
            go.Scatter(
                    x = df_macd['Date'],
                    y = df_macd['ema12'],
                    name = "EMA 12 Over Last " + str(numYearMACD) + " Year(s)"
                ),
            row=1, col=1
        )
    
    figMACD.add_trace(
            go.Scatter(
                    x = df_macd['Date'],
                    y = df_macd['ema26'],
                    name = "EMA 26 Over Last " + str(numYearMACD) + " Year(s)"
                ),
            row=1, col=1
        )
    
    figMACD.add_trace(
            go.Scatter(
                    x = df_macd['Date'],
                    y = df_macd['macd'],
                    name = "MACD Line"
                ),
            row=2, col=1
        )
    
    figMACD.add_trace(
            go.Scatter(
                    x = df_macd['Date'],
                    y = df_macd['signal'],
                    name = "Signal Line"
                ),
            row=2, col=1
        )
    
    figMACD.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="left",
        x=0
    ))
    
    figMACD.update_yaxes(tickprefix="$")
    st.plotly_chart(figMACD, use_container_width=True)
    
    st.subheader('Bollinger Band')
    coBoll1, coBoll2 = st.beta_columns(2)
    with coBoll1:
        numYearBoll = st.number_input('Insert period (Year): ', min_value=1, max_value=10, value=2, key=6) 
        
    with coBoll2:
        windowSizeBoll = st.number_input('Window Size (Day): ', min_value=5, max_value=500, value=20, key=7)
    
    startBoll= dt.datetime.today()-dt.timedelta(numYearBoll * 365)
    endBoll = dt.datetime.today()
    dataBoll = yf.download(ticker,startBoll,endBoll)
    df_boll = calcBollinger(dataBoll, windowSizeBoll)
    df_boll = df_boll.reset_index()
    figBoll = go.Figure()
    figBoll.add_trace(
            go.Scatter(
                    x = df_boll['Date'],
                    y = df_boll['bolu'],
                    name = "Upper Band"
                )
        )
    
    
    figBoll.add_trace(
                go.Scatter(
                        x = df_boll['Date'],
                        y = df_boll['sma'],
                        name = "SMA" + str(windowSizeBoll) + " Over Last " + str(numYearBoll) + " Year(s)"
                    )
            )
    
    
    figBoll.add_trace(
                go.Scatter(
                        x = df_boll['Date'],
                        y = df_boll['bold'],
                        name = "Lower Band"
                    )
            )
    
    figBoll.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="left",
        x=0
    ))
    
    figBoll.update_yaxes(tickprefix="$")
    st.plotly_chart(figBoll, use_container_width=True)
