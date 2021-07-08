import tweepy
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
        #Store data in a hashtable {User:Tweet(s)}
        parsedTweets = api.search(q=self.query + '-filter:retweets', count=self.count)
        
        for tweet in parsedTweets:
            #Get username
            user = '@'+tweet.user.screen_name

            if tweet.text not in self.data.values():
                #If we find users who have more than one tweet append the new tweet to a list
                if user in self.data.keys():
                    self.data[user] = list(self.data[user])
                    self.data[user].append(tweet.text)
                else:
                    self.data[user] = tweet.text