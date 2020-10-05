# Update A Record With SQLite: Have a look at 16-->17-->18-->19

from tkinter import *
#from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Learn from Balde.com')
#root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')
root.geometry("400x500")

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
    put_place text
)
""") 
'''
# Create Edit function to Update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        put_place= :put

        WHERE oid = :oid""", 
        {'put': f_name_editor.get(),

        'oid': record_id

        })
    
    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    #editor.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')
    editor.geometry("400x300")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the Database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
   
    
    # Create Global Variables for text box names
    global f_name_editor
    

    # Create text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

   


    # Create text Box Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    


     # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        

    # Create a Save Button To Save Edited Record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)




# Create Function to Delete A Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Delete a Record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()


# Create Fuction For Database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name)",
            {
                'f_name': f_name.get()
            })

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    
    # Clear The Text Boxes
    f_name.delete(0, END)
    

def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    # Loop through Results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)    

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()    

# Create text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))




delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

 
# Create text Box Labels
f_name_label = Label(root, text="Add tasks")
f_name_label.grid(row=0, column=0, pady=(10, 0))




delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)


# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# Commit Changes
conn.commit()

# Close connection
conn.close()


root.mainloop()