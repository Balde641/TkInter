# Drop Down Boxes

from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Section", command=show)
myButton.pack()

root.mainloop()