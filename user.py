from textblob import TextBlob

class user:
    def __init__(self, name, tweet, location, date):
        self.name = name
        self.tweet = tweet
        self.location = location
        self.date = str(date)
    
    def getSentiment(self):
        text = TextBlob(self.tweet)
        #Check polarity of tweet
        if text.polarity > 0:
            return('Positive')
        elif text.polarity == 0:
            return('Neutral')
        else:
            return('Negative')