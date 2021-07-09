import sqlite3

conn = sqlite3.connect('tweets.db')
c = conn.cursor()

def createDb():
    try:
        c.execute("""CREATE TABLE tweets (
                    Username text,
                    Tweet text,
                    Sentiment text,
                    Location text,
                    Date text)""")
    except:
        pass

def insertDb(user, tweet, sentiment, location, date):
    c.execute("INSERT INTO tweets VALUES (?, ?, ?, ?, ?)", (user, tweet, sentiment, location, date))

def displayDb():
    c.execute("SELECT * FROM tweets")
    print(c.fetchall())




