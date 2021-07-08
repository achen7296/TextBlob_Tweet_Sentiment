from textblob import TextBlob

def evalSentiment(tweet):
    #Check if user has many tweets
    if type(tweet) != list:
        text = TextBlob(tweet)
        #Test polarity of tweet
        if text.polarity > 0:
            return('Positive')
        elif text.polarity == 0:
            return('Neutral')
        else:
            return('Negative')
    else:
        #If user has many tweets return a list of evaluated polarities
        sentimentList = []
        for i in tweet:
            text = TextBlob(i)
            if text.polarity > 0:
                sentimentList.append('Positive')
            elif text.polarity == 0:
                sentimentList.append('Neutral')
            else:
                sentimentList.append('Negative')
        return sentimentList