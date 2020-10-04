

# Creating a login system with pictures

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("700x500")

        #===All Images
        self.bg_icon=ImageTk.PhotoImage(file="img3/log1.jpg")
        self.user_icon=ImageTk.PhotoImage(file="img3/userB.png")
        self.pass_icon=ImageTk.PhotoImage(file="img3/pas.jpg")
        self.pass2_icon=ImageTk.PhotoImage(file="img3/log.png")


        #====Variables==
        
        self.uname=StringVar()
        self.pass_=StringVar()
        
        bg_lbl=Label(self.root,image=self.bg_icon)
        bg_lbl.pack()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=200,y=70)

        #logolbl
        lbl_pass2=Label(Login_Frame,image=self.pass2_icon,bd=0)
        lbl_pass2.grid(row=0,columnspan=2, pady=20)

        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",15,"bold"),bg="white")
        lbluser.grid(row=1,column=0,padx=0,pady=0)
        textuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15))
        textuser.grid(row=1,column=1, padx=20)

        lbl_pass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",15,"bold"),bg="white")
        lbl_pass.grid(row=2,column=0,padx=20,pady=10)
        text_pass=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("",15))
        text_pass.grid(row=2,column=1, padx=20)
        
        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times now roman",14,"bold"),bg="yellow",fg="red")
        btn_log.grid(row=3,column=1,pady=10)


    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
             messagebox.showinfo("Error", "All fields are required!!")
        elif self.uname.get()=="Balde" and self.pass_.get()=="123":
             messagebox.showinfo("Successful",f"Welcome! {self.uname.get()}") 
        else:
            messagebox.showerror("Error","Invalid username or Password")         

root=Tk()
object=Login_System(root)
root.mainloop()        