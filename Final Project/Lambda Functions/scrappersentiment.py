# Yahoo
import numpy as np
import bs4 
import requests
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pandas import DataFrame
import time
import nltk
import plotly.express as px
nltk.download('vader_lexicon')

# Find News Function

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

df = findnewssentiment('Tesla')

df_pie = df[['Sentiment','Title']].groupby('Sentiment').count()
fig = px.pie(df_pie, values=df_pie['Title'], names=df_pie.index)
fig.show()