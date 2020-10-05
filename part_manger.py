from tkinter import *

# Create window object
app = Tk()

# Part
part_text = StringVar()
part_lable = Label(app, text='Part Name', font=('bold', 14), pady=20)
part_lable.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_lable = Label(app, text='Customer', font=('bold', 14))
customer_lable.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=part_text)
customer_entry.grid(row=0, column=3)

# Part
part_text = StringVar()
part_lable = Label(app, text='Part Name', font=('bold', 14))
part_lable.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Part
part_text = StringVar()
part_lable = Label(app, text='Part Name', font=('bold', 14))
part_lable.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Part
part_text = StringVar()
part_lable = Label(app, text='Part Name', font=('bold', 14))
part_lable.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

app.title('Part Manager')
app.geometry('700x350')

# Start program
app.mainloop()