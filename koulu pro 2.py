

# Creating a login system

from tkinter import *
from PIL import ImageTk


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("500x300")

        #===All Images
        self.bg_icon=ImageTk.PhotoImage(file="log1.jpg")
        self.user_icon=ImageTk.PhotoImage(file="login2.jpg")
        self.pass_icon=ImageTk.PhotoImage(file="user2.jpg")


        bg_lbl=Label(self.root,image=self.bg_icon)
        bg_lbl.pack()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=200,y=70)

        lbl_pass=Label(Login_Frame,image=self.pass_icon)
        lbl_pass.grid(row=0,column=0, pady=20)

        lbl_user=Label(Login_Frame,"Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"))
        lbl_user.grid(row=1,column=0,padx=20,pady=10)
        



root=Tk()
object=Login_System(root)
root.mainloop()        