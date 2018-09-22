import os

import twitter

auth = twitter.OAuth(consumer_key=os.environ['TWITTER_AUTH'],
consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
token=os.environ['TWITTER_TOKEN'],
token_secret=os.environ['TWITTER_TOKEN_SECRET'])

t = twitter.Twitter(auth=auth)

status=os.environ['TWEET']
t.statuses.update(status=status)
