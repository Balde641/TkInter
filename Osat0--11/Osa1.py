# Avaa UI kirjasto 
from tkinter import *

# TK() = uusi ikkuna. Soijoitetaan se muuttujan root.
root = Tk()

# Funktio nappulan painamisen käisittelyyn.
def IClinked():
    # Kirjoita tekstit Labeliin, joka sijoitetaan ikkunaan, nimeltä root.
    buttonClickLabel=Label(root, text="Nappulaa painettu")
    buttonClickLabel.pack()

# Esimerkki disabled nappulasta.
disabledButton = Button(root, text="Paina nappulaa", state=DISABLED)
disabledButton.pack()

# Esimerkki aktiivisesti nappulasta.
activeButton = Button(root, text="Paina nappulaa", padx=50, pady=50, command=IClinked, fg="red")
activeButton.pack()

# Käynistä root niminen ikkuna.
root.mainloop()