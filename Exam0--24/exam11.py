# Create New Windows in tKinter

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')

def open():
    global my_imag
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')
    my_imag = ImageTk.PhotoImage(Image.open("images 2nd/Balde8.png"))
    my_label = Label(top, image=my_imag)
    my_label.pack()

    btn2 = Button(top, text="Close Window", command=top.destroy)
    btn2.pack()

btn = Button(root, text="Open Second Window", command=open)
btn.pack()


root.mainloop()