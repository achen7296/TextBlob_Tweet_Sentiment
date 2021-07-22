import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = '5876688abc123'

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = 5432)
print("Database sucessfully connected")
c = conn.cursor()
display = conn.cursor(cursor_factory=RealDictCursor)

def createDb():
    try:
        c.execute("""CREATE TABLE tweets (
                    Date TEXT,
                    Username TEXT,
                    Tweet TEXT,
                    Sentiment TEXT,
                    Location TEXT)""")
        print("Database table sucessfully created")
    except:
        pass

def insertDb(d, u, t, l, s):
    postgres_insert_query = """ INSERT INTO tweets (Date, Username, Tweet, Sentiment, Location) VALUES(%s,%s,%s,%s,%s)"""
    record_to_insert = (d,u,t,l,s)
    try:
        c.execute(postgres_insert_query, record_to_insert)
    except:
        conn.rollback()

def displayDB():
    try:
        display.execute("SELECT * FROM tweets")
        return display.fetchall()
    except:
        conn.rollback()



