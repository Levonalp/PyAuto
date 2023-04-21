import tweepy
import os
from textblob import TextBlob
from jinja2 import Environment, FileSystemLoader

# Set up Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def fetch_tweets(brand, count=100):
    tweets = api.search(q=brand, count=count, lang='en', tweet_mode='extended')
    return tweets


def analyze_sentiment(tweets):
    sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}

    for tweet in tweets:
        text = tweet.full_text
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment['positive'] += 1
        elif polarity < 0:
            sentiment['negative'] += 1
        else:
            sentiment['neutral'] += 1

    return sentiment


def generate_report(brand, sentiment, template='report.html'):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template)

    with open(f"{brand}_report.html", 'w') as f:
        f.write(template.render(brand=brand, sentiment=sentiment))


def main():
    brand = input("Enter the brand name: ")
    tweet_count = int(
        input("Enter the number of tweets to analyze (default 100): "))
    print(f"Fetching and analyzing {tweet_count} tweets for {brand}...")
    tweets = fetch_tweets(brand, count=tweet_count)
    sentiment = analyze_sentiment(tweets)
    generate_report(brand, sentiment)
    print(f"Report generated: {brand}_report.html")


if __name__ == "__main__":
    main()
