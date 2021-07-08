import sqlite3

conn = sqlite3.connect('tweets.db')
c = conn.cursor()

def createDb():
    try:
        c.execute("""CREATE TABLE tweets (
                   Username text,
                   Tweet text,
                   Sentiment text)""")
    except:
        print("Database already initialized")

def insertDb(user, tweet, sentiment):
    c.execute("INSERT INTO tweets VALUES (?, ?, ?)", (user, tweet, sentiment))

def displayDb():
    c.execute("SELECT * FROM tweets")
    print(c.fetchall())




