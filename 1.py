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

st.set_page_config(page_title="TSA-1", page_icon=":tada:", layout="wide")
st.title('Twitter Sentiment Analysis')
st.subheader('Get Tweets')

consumerKey = "we0Drpnvc1FZNazKkiKoFWlGf"
consumerSecret = "OXRvmJwM6ca9k90XMIMoktSCa5XvjNieqJivcfjbOAlmpO6RhH"
accessToken = "501682241-ZG1DshytyxUIUY8FXPoH2AXaDG9d5DQlORemfAzU"
accessTokenSecret = "mxwCYkDjgWG5qWy8ONtVs3j2lxiYSxyberVVa92jmd27z"

#Appliyng tokenization
# def tokenization(text):
#     text = re.split('\W+', text)
#     return text

# #Removing stopwords
# stopword = nltk.corpus.stopwords.words('english')
# def remove_stopwords(text):
#     text = [word for word in text if word not in stopword]
#     return text
  
# #Appliyng Stemmer
# ps = nltk.PorterStemmer()

# def stemming(text):
#     text = [ps.stem(word) for word in text]
#     return text

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
  
  st.subheader("Here is the sample of our pre-processing on tweets")
  df['Tweets'] = df['Tweets'].apply(cleanTxt)
  st.write(df.head())

  df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
  df['Polarity'] = df['Tweets'].apply(getPolarity)
  df['Analysis'] = df['Polarity'].apply(getAnalysis)
  st.write(df.head())

  st.header('See what we have analysed')
  st.write(df['Analysis'].value_counts())

  chart_data = df.iloc[:,1:3]
  c = alt.Chart(chart_data).mark_circle().encode(alt.X("Polarity"),alt.Y("Subjectivity"))
  st.altair_chart(c, use_container_width=True)

  ptweets = df[df.Analysis == 'Positive']
  ptweets = ptweets['Tweets']
  ntweets = df[df.Analysis == 'Negative']
  ntweets = ntweets['Tweets']
  netweets = df[df.Analysis == 'Neutral']
  netweets = netweets['Tweets']
  
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
  
  st.subheader("Frequently used words in positive tweets")
  text = ' '.join([word for word in ptweets])
  plt.figure(figsize=(20,15), facecolor='None')
  wordcloud = WordCloud(max_words=500, width=1600,  height=800).generate(text)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.title('Most frequent words in positive tweets', fontsize=10)
  plt.show()
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()

  st.subheader("Frequently used words in negative tweets")
  text = ' '.join([word for word in ntweets])
  plt.figure(figsize=(20,15), facecolor='None')
  wordcloud = WordCloud(max_words=500, width=1600,  height=800).generate(text)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.title('Most frequent words in negative tweets', fontsize=10)
  plt.show()
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()
  
  st.subheader("Frequently used words in neutral tweets")
  text = ' '.join([word for word in netweets])
  plt.figure(figsize=(20,15), facecolor='None')
  wordcloud = WordCloud(max_words=500, width=1600,  height=800).generate(text)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.title('Most frequent words in neutral tweets', fontsize=10)
  plt.show()
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()
  
