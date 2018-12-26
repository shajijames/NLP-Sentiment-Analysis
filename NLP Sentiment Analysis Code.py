# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:39:08 2018

@author: SHAJI JAMES
"""

import tweepy
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
    
fetched_tweets = api.search(q = '#digitalindia', count = 100,lang='en')

tweets=[]
for tweet in fetched_tweets: 
    if tweet.retweet_count > 0: 
        if tweet.text not in tweets: 
            tweets.append(tweet.text) 
    else: 
        tweets.append(tweet.text)

len(tweets)

import re
def clean_tweet(tweet):
    return str.lower(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", ' ', tweet))

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

refined_tweets=[]
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
for tweet in tweets:
    tokens=word_tokenize(clean_tweet(tweet))
    word_list=[]
    for word in tokens:
        if word not in stop_words:
            word_list.append(lemmatizer.lemmatize(word, pos='v'))
    refined_tweet=' '.join(word_list)
    refined_tweets.append(refined_tweet)

polarity=0
positive=0
negative=0
neutral=0

from textblob import TextBlob
for tweet in refined_tweets:
    blob=TextBlob(tweet)
    polarity+=blob.sentiment.polarity
    if blob.sentiment.polarity>0:
        positive+=1
    elif blob.sentiment.polarity==0:
        neutral+=1
    else:
        negative+=1

print('Positive tweet percentage: ',(positive/len(tweets))*100)
print('Negative tweet percentage: ',(negative/len(tweets))*100)
print('Neutral tweet percentage: ',(neutral/len(tweets))*100)
