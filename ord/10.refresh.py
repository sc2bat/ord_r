# tab1 뽑기 tab2 대포 tab3 코드 저장 및 불러오기


import random 
import tkinter as tk
from random import *
from tkinter import *
from tkinter import ttk

x = []
tr = ["루피", "조로", "나미", "우솝", "상디", "쵸파", "로빈", "프랑키", "브룩", "샹크스", "검은수염", "시라호시", "아오키지", "아카이누", "키자루", "로우", "도플라밍고", "사보", "후지토라", "타시기", "루치", "바질 호킨스", "징베", "스네이크맨", "키드"]
im = ["로져", "레일리", "스코퍼 가반", "흰수염", "거프", "센고쿠", "시키", "드래곤", "제트", "카이도", "빅맘"]
et = ["에이스", "핸콕", "카번딧슈", "버기", "비비", "미호크", "오뎅"]

def result_ord():
    # pass
    if(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==1):
        x = tr + im + et
        print(random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==0):
        x = tr + im
        print(random.choice(x))
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

def on_write(*args):
    s = string.get()
    if len(s) > max_len:
        string.set(s[:max_len])

def randomresult():
    t = t2_ent.get()
    i = randrange(1, int(t))
    # print(i)
    t2_result.configure(text=str(i))

window = Tk()
window.title("Ord roulette")
window.geometry("320x240+300+100")
window.resizable(False, False)

#
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="1")
notebook.add(tab2, text="2")
notebook.pack(expand=True, fill="both")

Label(tab1, width=0, height=3).pack()
Label(tab2, width=0, height=0).pack()

# tab1 element
chkvar = IntVar()
checkbox = tk.Checkbutton(tab1, text="초월", variable=chkvar)
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = tk.Checkbutton(tab1, text="불멸", variable=chkvar2)
checkbox2.pack()

chkvar3 = IntVar()
checkbox3 = tk.Checkbutton(tab1, text="영원", variable=chkvar3)
checkbox3.pack()

t1_btn = tk.Button(tab1, text="뽑기", command=result_ord)
t1_btn.pack()


# tab2 element

max_len = 2
string = tk.StringVar(tab2)
string.trace_variable("w", on_write)

t2_ent = tk.Entry(tab2, textvariable=string, font = "Helvetica 44 bold", width=2)
t2_ent.pack()

t2_btn_result = tk.Button(tab2, text="대포", command=randomresult)
t2_btn_result.pack(pady=5)

t2_result = Label(tab2, text='', font = "Helvetica 30 bold", width=2)
t2_result.pack(pady=5)

window.mainloop()
