# def result_ord():
#     # pass 
#     if(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==1):
#         x = tr + im + et
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==1 and chkvar2.get()==1 and chkvar3.get()==0):
#         x = tr + im
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==1):
#         x = tr + et
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==1):
#         x = im + et
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==1 and chkvar2.get()==0 and chkvar3.get()==0):
#         x = tr
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==0 and chkvar2.get()==1 and chkvar3.get()==0):
#         x = im
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==1):
#         x = et
#         t1_result.configure(text=random.choice(x))
#     elif(chkvar.get()==0 and chkvar2.get()==0 and chkvar3.get()==0):
#         t1_result.configure(text="None")

import random
from random import choice

a = 1
b = 0
u = 0
x = []
y = [1, 2]
z = [3, 4]
# w = [5, 6]
# q = [7, 8]
# print(random.choice(y))

# for x in y:
#     if u == a:
#         t = x*y
#         t.append(y)
#     elif u == b:
#         # t = x*z
#         # t.append(x)
#         t = x

# print(t)
#     # print(random.choice(t))

if u == a:
    for x in y:
        t = x*y
        t.append(y)
# print(q)