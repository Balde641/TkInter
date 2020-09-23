# Sliders

from tkinter import *
from PIL import ImageTk,Image
#from tkinter import filedialog

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')

# Here is for the window size
#root.geometry("300x300")

# Widget slider vertical and horizontal below
vertical = Scale(root, from_=0, to=500)
vertical.pack()

# A button for the label to print the verdicalal output
def slide():
    my_label = Label(root, text=vertical.get())
    my_label.pack()
    # Here is how we control the whole window size
    root.geometry(str(vertical.get()) + "x300")

my_btn = Button(root, text="Click Me 1!", command=slide)
my_btn.pack()

#_______________________________________________________________
# A button for the label to print the horizontal output
def slide2():
    my_label = Label(root, text=horizontal.get())
    my_label.pack()
    # Here is how we control the whole window size
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

# This print the lable
# my_label = Label(root, text=horizontal.get())
# my_label.pack()


my_btn = Button(root, text="Click Me!", command=slide2)
my_btn.pack()

root.mainloop()