# 1 chi masala
# lst = [1, 2, 33, 5, 6, 7, 7]
# n = 8
# for i,v in enumerate(lst):
#     for i2,v2 in enumerate(lst):
#         # print(v,v2)
#         if v+v2==n:
#             print(i2)
# ------------------------------------------
# 2 chi masala
# lst = [1, 4, 6, 8]
# new=[i*2 for i in lst ]
# print(new)
# --------------------------------
# 3 chi masala ?
# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# new=[]

# for i in lst:
#     new.append(i[::2])
# print(new)
# -------------------------------------------------------
# 4 chi masala
# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]

# for i in lst.copy():
#     if i==():
#        lst.remove(i)
# print(lst)
# ---------------------------------------------------------
# 5 chi masala
# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# lst=sorted(lst,key=lambda x:float(x[1]),reverse =True)

# print(lst)
# -------------------------------------------------------------
# 6 chi masala
# s = "python 3.0"
# tpl=list(s)
# tpl=tuple(tpl)
# print(tpl)
# ----------------------
# 7 chi masala
# lst = [1, 2, 3, 4]

# prefix = "emp"
# lst=[prefix+str(i) for i in lst]

# print(lst)
# ------------------------------------
# 8 chi masala
# gap = "salom aziz qalaysan"
# gap=gap.split()
# gap=sorted(gap,key=lambda x:len(x))
# print(gap)
# -----------------------------------------
# 9 chi masala
# lst = [12, 'salom', 4.5, 'dunyo', True]
# for i in lst:
#     if type(i)!=str:
#         lst.remove(i)
# lst=sorted(lst)
# print(lst)
# --------------------------------------------
# 10 chi masala
# t = (-3, 5, 0, 9, -1, 4)
# new=[]
# for i in t:
#     if i>0:
#         new.append(i)
# new=tuple(new)
# print(new)
# ---------------------------
# 11 chi masala
# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# strings=[]
# numbers=[]

# for i in lst:
#     if type(i)==str:
#         strings.append(i)
#     elif type(i)==int:
#         numbers.append(i)
# strings=sorted(strings)
# numbers=sorted(numbers,reverse=True)
# print(strings)
# print(numbers)
# ---------------------------------------------
# 12 chi masala
# lst = [(3, 10), (1, 20), (2, 30)]
# lst=sorted(lst,key=lambda x:x[0])
# print(lst)
# -------------------------------------
# 13 chi masala
# lst = [1, 2, 3, 4]
# lst=[x*x for x in lst]
# print(lst)
# ----------------------------
# 14 chi masala ?
# lst = ['salom', 'dunyo', 'python']
# lst2=[x[0].upper for x in lst]


# print(lst2)
# --------------------------------------------
# 5 chi masala
# t = (1, 2, 3, 4, 5)
# natija=sum(t)
# print(natija)
# -----------------------------------------------
# Masala->Oson ?
# 1 chi masala
# n=int(input("Nehta raqam kiritasiz: " ))
# lst=[]
# for i in range(n):
#     lst.append(int(input()))
# print(lst)
# ----------------------------------------------
# 2 chi masala
# lst=[]
# count=0
# while True:
#     i=(input())
#     if i=="stop":
#         break
#     lst.append(int(i))
#     count+=1
# print(f"Soni: {count}")
# print(f"Ohirgisi: {lst[-1]}")
# print(f"Teskarisi: {lst[::-1]}")
# -----------------------------------------
# 3 chi masala
# lst=[]
# while True:
#     c=input()
#     if c=="stop":
#         break
#     lst.append(int(c))
# if int(input()) in lst:
#     print("ha bor")
# else:
#     print("bunday raqam yo'q")
# ----------------------------------------
# 4 chi masala
# lst=[3, 5, 6, 34, 78, 33, 23]
# lst.remove(3)
# lst.remove(23)
# print(sorted(lst))
# --------------------------------
# 5 chi masala
# lst=[3, 5, 6, 34, 78 ,33, 23]
# print(min(lst))
# lst.remove(min(lst))
# print(min(lst))
# ----------------------------------
# 6 chi masala


    



