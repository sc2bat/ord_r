# radio btn 1,2,3,4 넷 중 하나만 선택되는것

import random 
from tkinter import *

x = []
tr = ["루피", "조로", "나미", "우솝", "상디", "쵸파", "로빈", "프랑키", "브룩", "샹크스", "검은수염", "시라호시", "아오키지", "아카이누", "키자루", "로우", "도플라밍고", "사보", "후지토라", "타시기", "루치", "바질 호킨스", "징베", "스네이크맨", "키드"]
im = ["로져", "레일리", "스코퍼 가반", "흰수염", "거프", "센고쿠", "시키", "드래곤", "제트", "카이도", "빅맘"]
et = ["에이스", "핸콕", "카번딧슈", "버기", "비비", "미호크", "오뎅"]

# x = x + tr
# print(x)
# x = tr + im
# print(x)
# del im
# print(x)

def result_ord():
    # pass
    if(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==1):
        x = tr + im + et
        print(random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==0):
        x_im = tr + im
        print(random.choice(x_im))
    elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==1):
        x = tr + et
        print(random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==1):
        x = im + et
        print(random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==0):
        x = tr
        print(random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==0):
        x = im
        print(random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==1):
        x = et
        print(random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==0):
        print()


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
    # print(chkvar.get())
    # print(chkvar2.get())
    # print(chkvar3.get())
    # print(ord.get())
    result_ord()

btn = Button(window, text="click", command=btncmd)
btn.pack()

window.mainloop()
