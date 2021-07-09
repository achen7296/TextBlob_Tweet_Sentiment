from tkinter import *
from initdb import *
from client import client

root = Tk()
#Checks if database is created
createDb()

def execute():
    # Check if integer was entered
    try:
        int(num.get())
        numCheck.config(text = "Tweet data recorded")

        # Parse num of tweets based on query into class
        tweets = client(query.get(), num.get())
        users = tweets.dataHandler()

        # Insert data into database
        for user in users:
            insertDb(user.name, user.tweet, user.getSentiment(), user.location, user.date)

        # Delete entry
        num.delete(0,END)
        query.delete(0,END)

        # Commit changes to database
        conn.commit()

    except ValueError:
        numCheck.config(text = "Enter a valid integer")
        num.delete(0,END)

# Create text boxes
num = Entry(root, width=30)
num.grid(row=0, column=1, padx=20)

numCheck = Label(root, text='')
numCheck.grid(row=1, column=1, padx=20)

query = Entry(root, width=30)
query.grid(row=2, column=1, padx=20)

# Create text box labels
num_label = Label(root, text="Number")
num_label.grid(row=0, column=0, padx=20)
query_label = Label(root, text="Query")
query_label.grid(row=2, column=0, padx=20)

# Create submit button
search_btn = Button(root, text="Search for tweets", command=execute)
search_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

root.mainloop()

# Close database connection
conn.close()
