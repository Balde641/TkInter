from tkinter import *

root = Tk()             # luo uuden Tk-olion josta tulee ohjelman pääikkuna
root.title("Otsikkoni") # lisää ikkunaan otsikko

# rivi 0 -------------------------------------------
l = Label(root, text = "Name:")
l.grid(row = 0, column = 0)
e = Entry(root, width = 30)
e.grid(row = 0, column = 1)
# rivi 1 -------------------------------------------
l2 = Label(root, text = "Password:")
l2.grid(row = 1, column = 0)
e2 = Entry(root, width = 30, show = '*')
e2.grid(row = 1, column = 1)
# rivi 2 -------------------------------------------
b = Button(root, text = "Enter")
b.grid(row = 2, column = 1)


root.mainloop()         # pitää ikkunan näkyvissä kunnes tuhoamme sen