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

def cleanTxt(text):
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

account = st.text_input('Enter the username')
n = st.number_input('Enter the number')

go = st.button('Get Tweets')

if go:
  authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
  authenticate.set_access_token(accessToken, accessTokenSecret)
  api = tweepy.API(authenticate, wait_on_rate_limit = True)

  posts = api.user_timeline(screen_name = account, count = n, lang = "en", tweet_mode="extended")

  df = pd.DataFrame( [tweet.full_text for tweet in posts] , columns=['Tweets'])
  st.write('Showing the five recent tweets: \n')
  for tweet in posts[0:5]:
    st.write(tweet.full_text)
  
  df['Tweets'] = df['Tweets'].apply(cleanTxt)
  st.write(df.head())

  df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
  df['Polarity'] = df['Tweets'].apply(getPolarity)
  df['Analysis'] = df['Polarity'].apply(getAnalysis)
  st.write(df.head())

  st.subheader('See what we have analysed')

  chart_data = df.iloc[:,1:3]
  c = alt.Chart(chart_data).mark_circle().encode(alt.X("Polarity"),alt.Y("Subjectivity"))
  st.altair_chart(c, use_container_width=True)

  ptweets = df[df.Analysis == 'Positive']
  ptweets = ptweets['Tweets']
  ntweets = df[df.Analysis == 'Negative']
  ntweets = ntweets['Tweets']
  st.write(str(round( (ptweets.shape[0] / df.shape[0]) *100 , 1)) + '% of tweets are positive and ' 
           + str(round( (ntweets.shape[0] / df.shape[0]) *100 , 1)) + '% are negative')
