
import tweepy
from tweepy import OAuthHandler


TWITTER_APP_KEY = '<INSERT KEY>'
TWITTER_APP_KEY_SECRET = '<INSERT KEY SECRET>'
TWITTER_ACCESS_TOKEN = '<INSERT ACCESS TOKEN>'
TWITTER_ACCESS_TOKEN_SECRET = '<INSERT ACCESS TOKEN SECRET>'


auth = OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

 
api = tweepy.API(auth)


# # process or store JSON
# for status in tweepy.Cursor(api.home_timeline).items(10):
# 	process_or_store(status._json)

# # list all of our followers
# for friend in tweepy.Cursor(api.friends).item():
# 	process_or_store(friend._json)


# def process_or_store(tweet):
#  	print(json.dumps(tweet))