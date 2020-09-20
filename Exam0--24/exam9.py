# Radio Buttons

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde3.png')

r = IntVar()
r.set("2")

Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

root.mainloop()