# Logging in to the program

# import sqlite3
# from tkinter import *
# from tkinter import messagebox


# with sqlite3.connect("quite.db") as db:
#     cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
# cursor.execute("SELECT * FROM user")

# db.commit()
# db.close()

# class main():
#     def __init__(self,master):
#         self.master = master
#         self.username = StringVar()
#         self.password = StringVar()
#         self.n_username = StringVar()
#         self.n_password = StringVar()
#         self.widgets()

#     def login(self):
#         with sqlite3.connect("quite.db") as db:
#             cursor = db.cursor()

#         find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
#         cursor.execute(find_user,[(self.username.get()),(self.password.get())])
#         results = cursor.fetchall()

#         if results:
#             self.logf.pack_force()
#             self.head["text"] = self.username.get()
#             self.head['pady'] = 150

#         else:
#             ms.showerror("Oop!!","Username not marched!")        
    
#     def new_user(self):
#         with sqlite3.connect("quite.db") as db:
#             cursor = db.cursor()

#         find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
#         cursor.execute(find_user,[(self.username.get())])

#         if cursor.fetchall():
#             ms.showerror("Oop!", "Username Taken!!")

#         else:
#             ms.showerror('Success!!', "Account Created")
#             self.logf()

#         insert = 'INSERT INTO user(username,password) VALUES(?,?)'
#         cursor.execute(insert,[(self.n_username.get()),(self.n_password.get())])
#         db.commit() 

#     def log(self):
#         self.username.set("")
#         self.password.set("")
#         self.head['text'] = "Create Account"
#         self.logf.pack()

#     def cr(self):
#         self.n_username.set("")
#         self.n_password.set("")
#         self.logf.pack_forget()
#         self.cr.pack()               

#     def widgets():
#         self.head = Label(self.master,text=" LOGIN ",font = ('freesansbold',35),pady=40)
#         self.head.pack()

#         self.logf = Frame(self.master,padx = 10,pady = 10)
#         Label(self.logf,text = "Username: ",font = ('freesansbold',20),padx=5,pady=5).grid(sticky=W)
#         Entry(self.logf,textvariable = self.username,db=8,font = ('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
#         Label(self.logf,text = "Password: ",font = ('freesansbold',20),padx=5,pady=5).grid(row=0,column=1,sticky=W)
#         Entry(self.logf,textvariable = self.username,db=8,font = ('calibri',15,'bold')).grid(row=1,column=0,sticky=E)
#         Button(self.logf,text = "  Login  ",db=7,font = ("monaco",15,'bold'),padx=5,pady=5,command=self.login).grid(row=2)
#         Button(self.logf,text = "make new account",db=7,font = ("monaco",15,'bold'),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
#         self.logf.pack()

#         self.crf = Frame(self.master,padx = 10,pady = 10)
#         Label(self.crf,text = "Username: ",font = ('freesansbold',20),padx=5,pady=5).grid(sticky=W)
#         Entry(self.crf,textvariable = self.username,db=8,font = ('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
#         Label(self.crf,text = "Password: ",font = ('freesansbold',20),padx=5,pady=5).grid(row=1,column=1,sticky=W)
#         Entry(self.crf,textvariable = self.username,db=8,font = ('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
#         Button(self.crf,text = " Go to Login ",db=7,font = ("monaco",15,'bold'),padx=5,pady=5,command=self.new_user).grid(row=2)
#         Button(self.crf,text = "Create Account",db=7,font = ("monaco",15,'bold'),padx=5,pady=5,command=self.log).grid(row=2,column=1)
#         self.logf.pack()


# root = Tk()
# main(root)
# root.geometry("400x350+350+150")
# root.mainloop()        
