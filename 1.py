# %%writefile app.py
import streamlit as st
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
# from cleantext import clean
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

st.title("Twitter Sentiment Analysis")

consumerKey = "we0Drpnvc1FZNazKkiKoFWlGf"
consumerSecret = "OXRvmJwM6ca9k90XMIMoktSCa5XvjNieqJivcfjbOAlmpO6RhH"
accessToken = "501682241-ZG1DshytyxUIUY8FXPoH2AXaDG9d5DQlORemfAzU"
accessTokenSecret = "mxwCYkDjgWG5qWy8ONtVs3j2lxiYSxyberVVa92jmd27z"

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# Set the access token and access tokent secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# Create the API object while passing in the auth info
api = tweepy.API(authenticate, wait_on_rate_limit = True)

username = st.text_input("Enter the username of the person whose tweets you want to get analysed")

number = st.number_input("Enter the number of tweets")

# Extract 100 tweets from the twitter user
posts = api.user_timeline(screen_name =username, count = number, lang = "en", tweet_mode="extended")

# Create a dataframe with a column called Tweets
df = pd.DataFrame( [tweet.full_text for tweet in posts] , columns=['Tweets'])

# Show the first 5 rows of data
df.head()

# Clean the text

# Create a function to clean the tweets
def cleanTxt(text):
  text = re.sub('@[A-Za-z0-9]+', '', text) #Removed @mentions
  text = re.sub(r'#', '', text)            #Removing the # symbol
  text = re.sub(r'RT[\s]+', '', text)      #Removing RT
#   text = clean(text, no_emoji=True)        #Remove the emojis
  text = re.sub(r"\S*https?:\S*", "", text) #Remove the hyperlink
  
  return text

# Cleaning the text
df['Tweets'] = df['Tweets'].apply(cleanTxt)

# Show the cleaned text
df.head()

# Create a function to get the subjectivity
def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
  return TextBlob(text).sentiment.polarity

# Create two new columns
df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)

# Show the new dataframe with the new columns
df.head()

# Create a function to compute the negative, neutral and positive analysis
def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

df['Analysis'] = df['Polarity'].apply(getAnalysis)

# Show the dataframe
df.head()
