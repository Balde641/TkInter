# Build an Image Viewer App AND ----->
# Using Icons, Images, and Exit Buttons

from tkinter import *

#  The ImageTk is a Tkinter-compatible photo image. 
from PIL import ImageTk,Image

# The root window is created
root = Tk()

# The title name
root.title('Learn To Code at Tkinter')

# This makes an icon image next to the title
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde1.png')

# The images list 
my_img1 = ImageTk.PhotoImage(Image.open("images/Balde1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/Balde2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/Balde3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/Balde4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/Balde5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# It indicates from which image the display starts
my_label = Label(image=my_img2)
my_label.grid(row=0, column=0, columnspan=3)

# Function block for forward button
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Description how forward button operates
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # This function disables the back button when element 5 is reached
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    # The back button called to act on the screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Function block for back button
def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Description how back button operates
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # This function disables the back button when element 1 is reached
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # The back button called to act on the screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    

# It prints the three buttons function like "<</>>/exit"
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="exit program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Position of the three buttons below the image
button_back.grid(row=1, column=0)
button_exit.grid(row=1, columns=4)
button_forward.grid(row=1, column=2)

# That shows images on the screen 
root.mainloop()

