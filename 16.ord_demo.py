
import random
import tkinter as tk
from random import choice, randrange
from tkinter import *
from tkinter import ttk

tr = ["루피", "조로", "나미", "우솝", "상디", "쵸파", "로빈", "프랑키", "브룩", "샹크스", "검은수염", "시라호시", "아오키지", "아카이누", "키자루", "로우", "도플라밍고", "사보", "후지토라", "타시기", "루치", "바질 호킨스", "징베", "스네이크맨", "키드"]
im = ["로져", "레일리", "스코퍼 가반", "흰수염", "거프", "센고쿠", "시키", "드래곤", "제트", "카이도", "빅맘"]
et = ["에이스", "핸콕", "카번딧슈", "버기", "비비", "미호크", "오뎅"]
li = ["에넬", "크로커다일", "레베카", "샬롯 카타쿠리", "시노부", "킹", "레드필드"]

def result_ord():
    # pass 
    # 4
    if(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==1 and chkvar4.get()==1):
        x = tr + im + et + li
        t1_result.configure(text=random.choice(x))
    # 3
    elif(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==1 and chkvar4.get()==0):
        x = tr + im + et
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==0 and chkvar4.get()==1):
        x = tr + im + li
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==1 and chkvar4.get()==1):
        x = tr + et + li
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==1 and chkvar4.get()==1):
        x = im + et + li
        t1_result.configure(text=random.choice(x))
    # 2
    elif(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==0 and chkvar4.get()==0):
        x = tr + im
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==1 and chkvar4.get()==0):
        x = tr + et
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==1 and chkvar4.get()==0):
        x = im + et
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==0 and chkvar4.get()==1):
        x = tr + li
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==0 and chkvar4.get()==1):
        x = im + li
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==1 and chkvar4.get()==1):
        x = et + li
        t1_result.configure(text=random.choice(x))
    # 1
    elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==0 and chkvar4.get()==0):
        x = tr
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==0 and chkvar4.get()==0):
        x = im
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==1 and chkvar4.get()==0):
        x = et
        t1_result.configure(text=random.choice(x))
    elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==0 and chkvar4.get()==1):
        x = li
        t1_result.configure(text=random.choice(x))
    # 0
    elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==0):
        t1_result.configure(text="None")

# limit
def on_write(*args):
    s = string.get()
    if len(s) > max_len:
        string.set(s[:max_len])

# number roulette
def tab2result():
    t = t2_ent.get()
    i = randrange(1, int(t))
    t2_result.configure(text=str(i))

# frame
window = Tk()
window.title("Ord roulette")
window.geometry("320x240+300+100")
window.resizable(False, False)

# tab
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="초불영제")
notebook.add(tab2, text="대포")
notebook.pack(expand=True, fill="both")

Label(tab1, width=0, height=1).pack()
Label(tab2, width=0, height=0).pack()

# tab1 element
chkvar = IntVar()
checkbox = tk.Checkbutton(tab1, text="초월", variable=chkvar)
checkbox.pack()
checkbox.select()
checkbox.place(x=40, y=20)

chkvar2 = IntVar()
checkbox2 = tk.Checkbutton(tab1, text="불멸", variable=chkvar2)
checkbox2.pack()
checkbox2.select()
checkbox2.place(x=100, y=20)

chkvar3 = IntVar()
checkbox3 = tk.Checkbutton(tab1, text="영원", variable=chkvar3)
checkbox3.pack()
checkbox3.select()
checkbox3.place(x=160, y=20)

chkvar4 = IntVar()
checkbox4 = tk.Checkbutton(tab1, text="제한", variable=chkvar4)
checkbox4.pack()
checkbox4.select()
checkbox4.place(x=220, y=20)

t1_btn = tk.Button(tab1, text="뽑기",width=5, height=1, command=result_ord)
t1_btn.pack()
t1_btn.place(x=135, y=70)

t1_result = Label(tab1, text='', font = "Helvetica 35 bold", width=10)
t1_result.pack(pady=5)
t1_result.place(x=5, y=120)

# tab2 element
max_len = 2
string = tk.StringVar(tab2)
string.trace_variable("w", on_write)

t2_ent = tk.Entry(tab2, textvariable=string, font = "Helvetica 35 bold", width=2)
t2_ent.pack()

t2_btn_result = tk.Button(tab2, text="대포", width=9, height=2, command=tab2result)
t2_btn_result.pack(pady=5)

t2_result = Label(tab2, text='', font = "Helvetica 45 bold", width=2)
t2_result.pack(pady=5)

window.mainloop()
