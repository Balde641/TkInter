# Create New Windows in tKinter

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')

top = Toplevel()
my_imag = ImageTk.PhotoImage(Image.open("images/Balde3.png"))
my_label = Label(top, image=my_imag)
my_label.pack()

root.mainloop()