# f=open("test.txt","w")
# lst=[3,5,6,8,9,10]
# for i in lst:
#     if i%2:
#         f.write(f"{i} ")

# f.close()

# 1 chi masala
# f=open("test.txt")
# dct={}
# data=f.read().split('\n')
# for i in data:
#     if i.split(',')[-1]not in dct:
#         dct[i.split(",")[-1]]=1
#     else :
#         dct[i.split(",")[-1]]+=1
#         print(i.split(',')[-1])
# print(dct)
# --------------------
# 1 ni 2 si
# all=f.read().split("\n")
# visa=[]
# for i in all:
#     if "visa" in i:
#         visa.append(i)
# visa=sorted(visa,key=lambda x:x.split(',')[-1])

# print(visa)
# --------------------------------------------------
# 1 ni 3 chisi
# data=f.read().split('\n')
# a=[]
# for i in data:
#     if len(set(i.split(',')[0]))==10:
#         print(f"davlat: {i.split(',')[-1]},korxona: {i.split(',')[-2]},valyute: {i.split(',')[2]}\n")
# ---------------------------------------------------------------------
# 2 chi masala
# 2 ni 1 chisi
# f = open("test2.txt")

# for i in f.read().split('\n'):
#     for x in i.split(',')[2].split("-"):
#         if x.isdigit():
#             break
#     else:
#         print(i)

# f.close()
# # --------------------------------------------
# 2 ni 2 chisi
# f=open("test2.txt")


# dct = {}

# for i in f.read().split("\n"):
#     a = i.split(",")
#     email = a[0].split("@")
#     if email[1] not in dct:
#         dct[email[1]] = 1
#     else:
#         dct[email[1]] += 1

# print(dct)

# f= open("text3.txt")
# dct={}
# lst=[]

# for i in f.read().split('\n'):
#     lst.append(i.split(',')[0].split('@')[1])
   

# for i in lst:
#     dct[i]=lst.count(i)


# print(dct)


# f.close()

# ------------------------------------------------
# 3 ni 1 chisi almoast finished
# f=open("aholi.txt")
# lst=f.read().split("\n")
# new=[]
# data=[]
# men=[]
# for i in lst:
#     new.append(i.split(","))
# for i in new:
#     data.append(i[2].split("-"))
# for i in new:
#     if int(i[2].split("-")[-1])<=1976 and i[-1]=="true":
#         men.append(i)
# print(men)
# -------------------------------------------------------------
# 3 ni 2 chisi sucks
# f=open("aholi.txt")

# f=open("aholi.txt")
# lst=f.read().split("\n")
# new=[]
# data=[]
# men=[]
# dct={}
# year=[]
# for i in lst:
#     new.append(i.split(","))
# for i in new:
#     data.append(i[2].split("-"))

# for i in new:
#     year.append(int(i[2].split("-")[-1]))
# for i in new:
#     dct[year]=new.count(int(i[2].split("-")[-1]))
# print(dct)

                                            



    
    



