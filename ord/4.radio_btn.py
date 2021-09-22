# radio btn 1,2,3,4 넷 중 하나만 선택되는것

from tkinter import *

window = Tk()
window.title("ord roulette")
window.geometry("640x480+300+100")
window.resizable(False, False)

# label1 = Label(window, text="")
# label1.pack()

# background = PhotoImage(file="ord/background2.png")
# label2 = Label(window, image=background)
# label2.pack()

chkvar = IntVar()
checkbox = Checkbutton(window, text="초월", variable=chkvar)
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(window, text="불멸", variable=chkvar2)
checkbox2.pack()

chkvar3 = IntVar()
checkbox3 = Checkbutton(window, text="영원", variable=chkvar3)
checkbox3.pack()

# ord = IntVar
# btn_ord_tr = Radiobutton(window, value=1, variable=ord)
# btn_ord_tr.pack()

def btncmd():
    print(chkvar.get())
    # print(chkvar2.get())
    # print(chkvar3.get())
    # print(ord.get())

btn = Button(window, text="click", command=btncmd)
btn.pack()

window.mainloop()
