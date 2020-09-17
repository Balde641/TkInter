from tkinter import *
import sqlite3

# Kirjoitetaan tietokantaan uusi rivi
def submit():

    conn = sqlte3.connect("tasklist.db")

    c = conn.cursor

    # Insert into table 

    c.execute("INSERT INTO tasks VALUES (:task)",
    {
        'task' : task.get()
    })
# Commit changes 
conn.commit()

# Close connection
conn.close()

task.delete(0, END)

# Käynistä root niminen ikkuna.
root.mainloop()