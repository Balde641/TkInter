# Creating Input Fields

from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=10)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello + " I like you!")
    myLabel.pack()

myButton = Button (root, text="Enter your Stock Quote", command=myClick, fg="blue", bg="green")
myButton.pack()

root.mainloop()