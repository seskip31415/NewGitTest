#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 12:22:19 2018

@author: sophieskipper
"""
import twitter
import tweepy 
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

# Define the location id for the UK
WOEID = 23424975 
# Define language of tweets
LANG = "en"
# Define type of tweets we are after
TWEETS_TYPE = "recent"
# Define max number of tweets per trend
MAX_STATUSES = 1000

# API config
twitterConfig = {
	'token' : '',
	'token_secret' : '',
	'consumer_key' : '',
	'consumer_secret' : ''
}


# Init sentiment analysis object
analyzer = SentimentIntensityAnalyzer()
# Compound sentiment extraction use example
# exampleCompoundSentiment = analyzer.polarity_scores("I love cats and dogs")["compound"]
# print(exampleCompoundSentiment)
