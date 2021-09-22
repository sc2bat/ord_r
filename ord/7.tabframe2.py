
from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="1")
notebook.add(tab2, text="2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="test1", width=50, height=25).pack()
Label(tab2, text="test2", width=50, height=25).pack()

window.mainloop()
