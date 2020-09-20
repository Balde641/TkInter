# Adding Frames To Your Program

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde2.jpg')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)  #it does the same job as below
#frame.grid(row=0, column=0)


b = Button(frame, text="Don't click here!")
b.grid(row=0, column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=1, column=1)


root.mainloop()