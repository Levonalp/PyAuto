import tweepy
from datetime import datetime, timedelta
import time

# Twitter Developer Account credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticating to the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Time to post (e.g., one hour from now)
post_time = datetime.now() + timedelta(hours=1)

# Content to post
content = "This is a scheduled post!"

# Function to post a tweet


def post_tweet(content):
    api.update_status(content)
    print("Tweet posted!")

# Function to get tweet metrics


def get_tweet_metrics(tweet_id):
    tweet = api.get_status(tweet_id)
    retweets = tweet.retweet_count
    favorites = tweet.favorite_count
    print(f"Retweets: {retweets}, Favorites: {favorites}")


# Main loop
while True:
    if datetime.now() >= post_time:
        tweet = post_tweet(content)
        time.sleep(60)  # Wait for 1 minute
        get_tweet_metrics(tweet.id)
        break
    time.sleep(60)  # Check every minute
