from tweepy import Stream
from tweepy.streaming import StreamListener

import tweepy
from tweepy import OAuthHandler

TWITTER_APP_KEY = '<INSERT KEY>'
TWITTER_APP_KEY_SECRET = '<INSERT KEY SECRET>'
TWITTER_ACCESS_TOKEN = '<INSERT ACCESS TOKEN>'
TWITTER_ACCESS_TOKEN_SECRET = '<INSERT ACCESS TOKEN SECRET>'


auth = OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
 
api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('hash_tag_data.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s&" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['<INSERT HASHTAG>'])
 
