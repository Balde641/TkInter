# (tk3.py), Esimerkki (tk4.py), Esimerkki (tk5.py), Esimerkki (tk6.py)

from tkinter import *
root = Tk()             
root.title('Quiz')



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


q1 = 'Favourite colour: '
q2 = 'Favourite dessert: '
q3 = 'Favourite book: '
q4 = 'Favourite pet: '

l = Label(root, text = 'My favourite things', fg = '#006699', font = ('Comic Sans', 16, 'bold'))
l.grid(row = 0, column = 0, columnspan = 2)

list = [q1, q2, q3, q4]
rownum = 1
colnum = 0

for q in list: 
    l = Label(root, text = q)
    l.grid(row = rownum, column = colnum, pady = 2, sticky = W)
    entry = Entry(root, width = 20)
    entry.grid(row = rownum, column = colnum+1, pady = 2)
    rownum += 1
    colnum = 0

b = Button(root, text = 'Submit', bg = '#CCCCCC')
b.grid(row = rownum, column = 0, columnspan = 2, sticky = EW)



q = 'What is your favourite \n subject at school?'
l = Label(root, text = q, font = ('Verdana', 16, 'bold'), fg = 'red')
l.grid()

a1 = Button(root, text = 'Programming')
a1.grid()
a2 = Button(root, text = 'Math', state = DISABLED)
a2.grid()
a3 = Button(root, text = 'Physics', state = DISABLED)
a3.grid()
a4 = Button(root, text = 'English', state = DISABLED)
a4.grid()

label = Label(root, text = "Name: ")
# Entry luo kentän/rivin johon voi kirjoittaa tekstiä
# width määrää rivin pituuden 
name = Entry(root, width = 30)
button = Button(root, text = "Enter")

label.grid()
name.grid()
button.grid()

root.mainloop()