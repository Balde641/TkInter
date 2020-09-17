from tkinter import *
import sqlite3

root = Tk()
root.title("Tietokanta")
root.geometry("400x400")
query_label = Label(root)

# Kutsutaan Näytä tehtävät -nappulalla

def query():
    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    c.execute("SELECT task, oid FROM tasks")
    records=c.fetchall()

    print_records = ''

    for record in records:
        print_records += str(record[0]) + " \t " + str(record[1]) + " \n"

    heading_label = Label(root, text="Helvetica", font=("Helvetica", 16))

    heading_label['text'] = "Tehtävä \t ID"
    heading_label.grid(row=8, column=0, columnspan=2)

    query_label['text'] = print_records
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()

    conn.close()    