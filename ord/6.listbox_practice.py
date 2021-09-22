# radio btn 1,2,3,4 넷 중 하나만 선택되는것

import random 
from tkinter import *

x = []
tr = ["루피", "조로", "나미", "우솝", "상디", "쵸파", "로빈", "프랑키", "브룩", "샹크스", "검은수염", "시라호시", "아오키지", "아카이누", "키자루", "로우", "도플라밍고", "사보", "후지토라", "타시기", "루치", "바질 호킨스", "징베", "스네이크맨", "키드"]
im = ["로져", "레일리", "스코퍼 가반", "흰수염", "거프", "센고쿠", "시키", "드래곤", "제트", "카이도", "빅맘"]
et = ["에이스", "핸콕", "카번딧슈", "버기", "비비", "미호크", "오뎅"]

def result_ord():
    # pass
    if(chkvar.get()==1 and chkvar3.get()==1):
        x = tr
        print(random.choice(x))
    elif(chkvar2.get()==1):
        x = im
        print(random.choice(x))
    elif(chkvar.get()==0):
        x = []
        print()

def btncmd():
    result_ord()        

window = Tk()
window.title("ORD roulette")
window.geometry("640x480+300+100")
window.resizable(False, False)

chkvar = IntVar()
checkbox = Checkbutton(window, text="초월", variable=chkvar)
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(window, text="불멸", variable=chkvar2)
checkbox2.pack()

chkvar3 = IntVar()
checkbox3 = Checkbutton(window, text="영원", variable=chkvar3)
checkbox3.pack()

btn = Button(window, text="뽑기", command=btncmd)
btn.pack()

window.mainloop()
