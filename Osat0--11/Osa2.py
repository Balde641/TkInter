# Messageboxin tekeminen
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Messagebox-hajoitus")

# Testaile messageboxin vaihtoehtoja: showinfo, showwarning, askquestion, asokcancel, eyes
def popup():
    response = messagebox.askyesno("Messagebox haluaa sanoa: ", "Täällä ollaan")
    # Jos käyttäjä painaa Yes:
    if response == 1:
        Label(root, text="Painoit Yes-nappia!").pack()
    # Jos käyttäjä painaa No:
    else:
        Label(root, text="Painoit No-nappia!").pack()

# Nappula, joka kutsuu funktiota popup
Button(root, text="Viesti", command=popup).pack()
root.mainloop()         
