from tkinter import *

window = Tk()
window.title("ord roulette")
window.geometry("640x480+300+100")
window.resizable(False, False)

# label1 = Label(window, text="")
# label1.pack()

background = PhotoImage(file="ord/background2.png")
label2 = Label(window, image=background)
label2.pack()

window.mainloop()
