# Open Files Dialog Box

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')

# Here we rae going directly to the file

# root.filename = filedialog.askopenfilename(initialdir="/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png", 
# title="Select a File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
# my_label = Label(root, text=root.filename)
# my_label.pack()

# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image)
# my_image_label.pack()


# Here we use a button on GUI to reach the file
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png", 
    title="Select a File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()

# This is the button we press to go to the the file
my_btn = Button(root, text="Open File", command=open)
my_btn.pack()



root.mainloop()