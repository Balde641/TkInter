# Checkboxes

from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')
root.geometry("400x400")

def show():
    # To see if bos is checked
    myLabel = Label(root, text=var.get())
    myLabel.pack()


var = StringVar() 

c = Checkbutton(root, text="Would you like to SuperSize your order? Check Here!", 
variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()


myButton = Button(root, text="Show Section ", command=show)
myButton.pack()

root.mainloop()


