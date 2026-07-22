#  Mustaqil ish
# 1 chi misol
# lst=[5,12,7,9]
# print(max(lst))
# -----------------------
#  2 chi misol
# lst=[4,2,7,1]
# print(min(lst))
# ---------------------------
#  3 chi misol
# lst=[2,4,6]
# average=sum(lst)
# average=average//3
# print(average)
# ----------------------------
# 4 chi misol
# lst=(1,2,3)
# print(sum(lst))
# -------------------------------
# 5 chi misol
# a=(3,1,4)
# b=max(a)
# c=min(a)
# print(b,c)
# -------------------------------
# 6 chi misol ?
# lst=int(input("lst: "))
# lst2=lst.sort()
# print(lst2)
# -------------------------------
# 7 misol
# lst=[1,2,3,4]
# teskari=lst.copy()
# teskari.reverse()
# print(teskari)
# -------------------------
# 8 chi misol
# tpl=(1,2,3)
# for i in tpl:
#     i+=i
#     print(i,end="")
# -------------------------------
# 9 chi misol
# lst=[1,2,3,4,5,6]
# lst2=[]
# for i in lst:
#     if i%2==0:
#         lst2.append(i)
# print(lst2)
# ----------------------------------
# 10 chi misol
# lst=[1,2,3,4,5,6]
# lst2=[]
# for i in lst:
#     if i%2:
#         lst2.append(i)
# print(lst2)
# ------------------------------------
# 11 chi misol
# tpl=(1,'a',3.5,2)
# for i in tpl:
#     if type(i)==int:
#         print(i)
# -----------------------------
# 12 chi misol
# lst=[1,2,3]
# new=[]
# for i in lst:
#     new.append(i**3)
# print(new)
# ---------------------------------
# 13 chi misol
# lst=[1,2,2,3,3,3]
# new=[]
# for index,variable in enumerate(lst):
    # if variable==index+1:
    #     new.append(variable)
    # count=0
    # if variable==index+1:
    #     count+=1
    #     if count==1:
    #         print(variable)
    #         new.append(variable)
# for i in lst:
#     if i not in new:
#         new.append(i)
# print(new)
# -----------------------------------------------
#  14 chi misol
# tpl=(1,2,3)
# new=[]
# for i in tpl:
#     new.append(str(i))
# print(new)
# ----------------------------------------
# 15 chi misol
# lst=['a','b']
# for index ,variable in enumerate(lst):
#     print(f"{index},{variable} ",end="")
# -----------------------------------------------
# Uyga vazifa
# 1 chi misol
# lst=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# count=0
# for i in lst:
#     if type(i)==int:
#         count+=1
# print(count)
# ------------------------------------------------------------------
# 2 chi misol
# lst=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# m=[]
# for i in lst:
#     if type(i)==int:
#          m.append(i)
# print(max(m))
# ----------------------------------------------------------------
# 3 chi misol
# lst=['abc', 'xyz', "bo'lib", 'aba', '1221']
# count=0
# for i,variable in enumerate(lst):
#     if variable [0]==variable[-1]:
#         count+=1
# print(count)
# ---------------------------------------------
#  4 chi misol
# lst=[True, "Salom", 5, 5.6]
# for i in lst:
#     print(f"{type(i)}",end=",")
# -------------------------------------
# 5 chi misol
# lst=[7, 8, 1, 3, 4, 6, 7, 5]
# new=[]
# for i,v in enumerate(lst.copy()):
#     if i%2:
#         new.append(v**3)
#     else:
#         new.append(v**2)
# print(new)
# ----------------------------------
# 6 chi misol
# lst=[2, 1, -4, -9, 0, -5, 8, 3]
# m=max(lst)
# lst.remove(m)
# print(max(lst))
# -----------------------------------
# 7 chi misol
# lst=[1, 1, 3, 4, 4, 5, 6, 7]
# lst2=[0, 1, 2, 3, 4, 4, 5, 7, 8]

# n1=sum(lst)
# n2=sum(lst2)
# final=n1+n2

# len1=len(lst)
# len2=len(lst2)

# print(len1)
# print(len2)
# final2=len1+len2

# print(final)
# print(final2)

# natija=final/final2
# print(natija)
# --------------------------------------
# 8 chi misol
# lst=["ada", 212, False, 4567, "aziza"]
# for i in lst:
#     s=str(i)
#     if s==s[::-1]:
#         print(f"{i}->polindrom")
#     else:
#         print(f"{i}->polindrom emas")
# -----------------------------------------
# 9 chi misol
# lst=['p', 'q']
# new=[]
# n=int(input("n ni kiriting: "))

# for i in range(1,n+1):
#     for x in lst:
#         new.append(x+str(i))
#         print(i)
# print(new)
# -------------------------------------
# 10 chi misol
# lst=[12, 9, 8, 1]
# if lst==sorted(lst):
#     print("o'sish tartibi")
# elif lst==sorted(lst,reverse=True):
#     print("kamayish tartibi")
# else:
#     print("tartibsiz")
# -------------------------------------------
# 11 chi misol
# lst=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# nol=[]
# nolmas=[]
# for i in lst:
#     if i!=0:
#         nolmas.append(i)
#     elif i==0:
#         nol.append(i)
# print(f"{nolmas+nol}")
# ----------------------------------------------
# # 12 chi misol
# lst=[[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# for i ,v in enumerate(lst):
#     for i2,v2 in enumerate(v):
#         if i2%2:
#             lst[i][i2]=v2*v2
# print(lst)
# print(lst)
# lst = [[2, 15, 4],
#        [19, 24, 11],
#        [7, 9, 5],
#        [10, 3, 1]]

# for row in lst:
#     print(row[1])
#     row[1] = row[1] ** 2

# print(lst)
# -----------------------------------------
# 13 chi misol
# lst=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# for i in lst:
#     s=str(i)
#     if s=="600":
#         lst=i.append("700")
# print(lst)


# lst=['9','9','9']
# sum=0

# for i in lst:
#     sum=sum*10+int(i)
#     print(sum)
# sum+=1
# natija=list(str(sum))

# print(natija)
# lst = [[1,2,3],[99],[2,2],[5,2]]

# natija = max(lst, key=lambda x: sum(x) if len(x)>1 else 0)

# print(natija)


# lst=[("olma", "ananas", "banan", 'anor')]

# if print(lst)!=lst.sort:
#     print("hs")
# lst = [True, "Salom", 5, 5.6]

# for index, i in enumerate(lst):
#     lst[index] = type(i)

# print(lst)
# lst = ['32', '9', '123', '996', '1024', '1999', '46']

# natija = max(lst, key=len)
# natija = max(lst, key=int)
# natija = max(lst, key=max)
# natija = max(lst, key=lambda x: x[::-1])
# natija = max(lst, key=lambda x: sum([int(i) for i in x]))
# natija = max(lst, key=lambda x: eval("+".join(list('123'))))
# print(natija)

# natija = sorted(lst, key=lambda x: x.count('9'), reverse=True)
# print(natija)

# tpl = tuple() # ()
# tpl = ("salom",34)
# tpl2 = (1,2,3,4)
# tpl3 = tpl + tpl2


# tpl = (1, 2, 54, 23, 12)

# tpl[-1] = "Karim"

# print(tpl)


lst = ['32', '9', '123', '996', '1024', '1999', '46']





