# from tkinter import *

# root = Tk()
# root.title("Alasvetovalikko")
# root.geometry("400x400")

# Tietokantakäsittelyä, lisäämistä, mukkaamista, poistamista

# Ensimmäiseksi avautuvan ikkunan näkymä
task_label = Label(root, text="Tehtävä")
task_label.grid(row=0, column=0, pady=(10,0))

task = Entry(root, width=30)
task_grid.grid(row=0, column=1, padx=20, pady=(10,0))

submit_btn =Button(root, text="Lisää tehtävä tietokantaan", command=submit)
submit_btn.grid(row=2, colum=0, columspan=2, pady=10, padx=10) #¢

query_btn = Button(root, text="Näytä tehtävät", command=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

select_label = Label(root, text="Valitse ID")
select_label.grid(row=4, column=0, pady=5)

delete_box = Entry(root, width=30)
delete_box.grid(row=4, column=1, pady=5)

delete_btn = Button(root, text="Poista tehtävä", command=delete)
delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

edit_btn = Button(root, text="Mukkaa tehtävää", command=edit)
edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()

