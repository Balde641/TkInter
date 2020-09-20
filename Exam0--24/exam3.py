# Creating Buttons

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I cliked a Button!!")
    myLabel.pack()

myButton = Button (root, text="Click Me", command=myClick, bg="red", fg="green")
myButton.pack()

root.mainloop()