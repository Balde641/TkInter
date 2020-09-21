# Radio Buttons

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde3.png')

#r = IntVar()
#r.set("2")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroon", "Mushroon"),
    ("Onion", "Onion")
]

pizz = StringVar()
pizz.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizz, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizz.get())
#myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizz.get()))
myButton.pack()

root.mainloop()