#  4 chi misol
# yosh=int(input("yoshingizni kiriting: "))
# yil=int(input("Obuna bo'lish yillari: "))

# if yosh>50 and 5>yil>3:
#     print(f"""Asosiy narx: $15
# Yosh bo'yicha chegirma: 20%
# Obuna davomiyligi bo'yicha chegirma:10%
# Yakuniy narx: ${15-(15*30)/100} """)
# elif 5<yil :
#     print(f"""Asosiy narx: $15
# Yosh bo'yicha chegirma: 20%
# Obuna davomiyligi bo'yicha chegirma:15%
# Yakuniy narx: ${15-(15*35)/100} """)
# ------------------------------------------
# 5 chi misol
# while True:
#     parol=input("parol kiriting: ")
#     if len(parol)<8:
#         print("Kamida 8 ta belgi  kiritilishi shart!")
#         break
#     elif parol in ("ASDFGHJKLOPIUYTREWQZXCVBNM")==-1:
#         print("Kamida 1 ta katta harf kiritilishi shart!")
#         break
#     elif parol in ("#@$")==-1:
#         print("Kamida 1 ta maxsus belgi kiritnlishi shart!")
#         break
#     elif parol in ("1234567890")==-1:
#         print("Kamida 1 ta raqam kiritnlishi shart!")
#         break
#     else :
        # print("parol kuchli!")
# ------------------------------------------------------------------
# 6 chi misol ?
# lst=[]
# for i in range(1,4):
#     kompaniya=(input(f"{i} Kompaniya nomini kiritint: "))
#     narx=int(input(f"{i} Narxni kiriting: "))
#     if narx>100:
#         lst.append(f"{kompaniya} aktsiyasi qimmat.")
#     elif narx<50:
#         lst.append(f"{kompaniya} aktsiyasi arzon.")
#     else:
#         lst.append(f"{kompaniya} aktsiyasi o'rtacha.")

# for i in lst:
    # print(i)
# -----------------------------------------------------------
# 1 chi misol 
# n=int(input("n ni kiriting: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i*i
#     print(f"{i} * {i} = {i*i}")
# print(sum)



# -------------------------------------------------
# 2 misol
# yosh=int(input("yoshingizni kiriting: "))
# for i in range(200):
#     if i==yosh:
#         print(f"{i} bu sizning yoshingiz")
#         break
#     else:
#         print(i)
# -------------------------------------------------
# 3 chi misol
for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100
    # if a==b!=c or a!=b==c or b!=a==c!=b:
            # print(i)
            
    # 2 chi usul if not a==b==c:
    #     if a==b or a==c or b==c:
    #         print(i)

# ---------------------------------------------------
# 4 chi misol
# import random
# son=random.randint(1,4)


# for i in range(3):
#     user=int(input("son kiriting"))
#     if son==user:
#         print("winner")
#         break
#     else:
        # print("looser")