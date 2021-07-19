from initdb import *
from client import client
from flask import Flask, request, render_template, redirect

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    #Checks if database is created
    createDb()
    print("Sucessfuly redirected to homepage")
    return render_template("index.html")

@app.route('/database')
def database():
    return render_template("database.html")

@app.route('/visualization')
def visualization():
    return render_template("visualization.html")

@app.route('/submit', methods =["GET", "POST"])
def submit_post():
    # Check if integer was entered
    if  request.method == 'POST':
        print("Post request recieved")
        try:
            query = request.form["q"]
            num = request.form["n"]
            num = int(num)
            print("These are the values for query and num " + str(query) + str(num))

            # Parse num of tweets based on query into class
            tweets = client(query, num)
            users = tweets.dataHandler()

            # Insert data into database
            for user in users:
                insertDb(user.date, user.name, user.tweet, user.getSentiment(), user.location)
                print("Sucessfully placed " + str(user.name) + " into the database")

            # Commit changes to database
            conn.commit()

            return render_template("index.html")

        except ValueError:
            print("Could not read query")
            return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

