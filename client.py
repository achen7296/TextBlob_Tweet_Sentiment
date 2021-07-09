import tweepy
from user import user
from pprint import pprint

consumer_key = 'eBKSNsuffFGsACqyysXPWKxRW'
consumer_key_secret = 'cA1XKwamNZffGH3kwnPOUqzGxvmHNBv2FnGQuheuOfyWK2t83r'

access_key = '1244001951437783042-aGFfqnQ2DyJ1Fvb8mg10TZHV3lz1gZ'
access_key_secret = 'mKiveaLNNn4ouf9h2eiDLyZ9izc0yvZ9h67F2TjabCWkP'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_key, access_key_secret)

api = tweepy.API(auth)

class client:

    def __init__(self, query='', count=10, data ={}):
        self.query = query
        self.count = count
        self.data = data

    def searchTweets(self):
        parsedTweets = api.search(q=self.query + '-filter:retweets', count=self.count)
        return(parsedTweets)
        
    def dataHandler(self):
        #Array of user objects to be returned
        users = []
        tweets = self.searchTweets()
        for tweet in tweets:
            #Convert tweet data into a user object
            userObj = user('@'+tweet.user.screen_name, tweet.text, tweet.user.location, tweet.created_at)
            users.append(userObj)
        return users