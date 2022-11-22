# %%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
import re
import tweepy
import altair as alt
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

st.title('Twitter Sentiment Analysis')
st.subheader('Get Tweets')

consumerKey = "we0Drpnvc1FZNazKkiKoFWlGf"
consumerSecret = "OXRvmJwM6ca9k90XMIMoktSCa5XvjNieqJivcfjbOAlmpO6RhH"
accessToken = "501682241-ZG1DshytyxUIUY8FXPoH2AXaDG9d5DQlORemfAzU"
accessTokenSecret = "mxwCYkDjgWG5qWy8ONtVs3j2lxiYSxyberVVa92jmd27z"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def cleanTxt(text):
  text = re.sub('RT @\w+: '," ",text)
  text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text)
  text = re.sub('@[A-Za-z0-9]+', '', text) #Removed @mentions
  text = re.sub(r'#', '', text)            #Removing the # symbol
  text = re.sub(r'RT[\s]+', '', text)      #Removing RT
  text = re.sub(r"\S*https?:\S*", "", text) #Remove the hyperlink
  
  return text

def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
  return TextBlob(text).sentiment.polarity

def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

keyword = st.text_input('Enter the keyword')
n = st.number_input('Enter the number of tweets')

go = st.button('Get Tweets')

if go:

  posts = tweepy.Cursor(api.search_tweets, tweet_mode = 'extended', q=keyword, lang = "en").items(n)

  df = pd.DataFrame( [tweet.full_text for tweet in posts] , columns=['Tweets'])
  
  df['Tweets'] = df['Tweets'].apply(cleanTxt)
  st.write(df.head())

  df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
  df['Polarity'] = df['Tweets'].apply(getPolarity)
  df['Analysis'] = df['Polarity'].apply(getAnalysis)
  st.write(df.head())

  st.header('See what we have analysed')

  chart_data = df.iloc[:,1:3]
  c = alt.Chart(chart_data).mark_circle().encode(alt.X("Polarity"),alt.Y("Subjectivity"))
  st.altair_chart(c, use_container_width=True)

  ptweets = df[df.Analysis == 'Positive']
  ptweets = ptweets['Tweets']
  ntweets = df[df.Analysis == 'Negative']
  ntweets = ntweets['Tweets']
  
  plt.title('Sentiment Analysis')
  plt.xlabel('Sentiment')
  plt.ylabel('Counts')
  df['Analysis'].value_counts().plot(kind='bar')
  plt.show()
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()

  colors = ("yellowgreen", "gold", "red")
  wp = {'linewidth':2, 'edgecolor':"black"}
  tags = df['Analysis'].value_counts()
  explode = (0.1,0.1,0.1)
  tags.plot(kind='pie', autopct='%1.1f%%', shadow=True, colors = colors,
            startangle=90, wedgeprops = wp, explode = explode, label='')
  plt.title('Distribution of sentiments')
  plt.show()
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()
