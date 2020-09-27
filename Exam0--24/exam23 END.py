# Koulu projekti osa2

from tkinter import *
import sqlite3

root = Tk()
root.title('Tietokanta')
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect('tasklist.db')

# Create a cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE asiat (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode interger
)
""")

# Commit Changes
conn.commit()

# Close connection
conn.close()


root.mainloop()