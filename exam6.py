# Using Icons, Images, and Exit Buttons

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Tkinter')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/Balde-love-heart.png')

my_img = ImageTk.PhotoImage(Image.open("images/Balde-i-love-u.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Progaram ", command=root.quit)
button_quit.pack()


root.mainloop()

