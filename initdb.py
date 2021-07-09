import sqlite3

conn = sqlite3.connect('tweets.db')
c = conn.cursor()

def createDb():
    try:
        c.execute("""CREATE TABLE tweets (
                    Date text,
                    Username text,
                    Tweet text,
                    Sentiment text,
                    Location text)""")
    except:
        pass

def insertDb(date, user, tweet, location, sentiment):
    c.execute("INSERT INTO tweets VALUES (?, ?, ?, ?, ?)", (date, user, tweet, location, sentiment))

def displayDb():
    c.execute("SELECT * FROM tweets")
    print(c.fetchall())




