# 1 chi misol
# oylar={

#      "yanvar":"01",
#      "fevral": "02",
#      "mart" : "03",
#      "aprel":"04",
#      "may": "05",
#      "iyun" : "06",
#      "iyul":"07",
#      "avgust": "08",
#      "sentyabr" : "09",
#       "oktyabr":"10",
#      "noyabr": "11",
#      "decabr" : "12"
# }
# user=input("sana kiriting: ")
# user=user.split()
# print(user)
# print(f"{user[0]}.{oylar[user[1]]}.{user[2][-3:]}")
# -----------------------------------------------------------
# 2 chi misol
# numbers=[3,7,12,7,5,3,9,12,15,7]
# numbers=sum(tuple(set(numbers)))/len(tuple(set(numbers)))
# print(numbers)
# ----------------------------------------------------------
# 3 chi misol
# import json
# products={
#     "olma":12000,
#     "banan":18000,
#     "shaftoli":15000,
#     "uzum":20000
# }
# nom=input("mahsulot nomini kiriting: ")
# miq=int(input("mahsulot miqdorini kiriting: "))
# if nom in products:
#     narx=products[nom]*miq
#     dct={
#         "mahsulot":nom,
#         "miqdor":miq,
#         "narx":narx
#     }
#     print(f"umumiy narx={narx}")
#     with open("mock.json","w") as f:
#         json.dump(dct,f,indent=4)
# else:
#     print("Bunday mahsulot mavjud emas!")
# ------------------------------------------------------
# 4 chi misol
# 1 chi
# def eng_uzun(matn:str):
#     return max(matn.split(),key=len)

# matn="Foydalanuvchidan eng uzun matn kiriting"
# print(natija:=eng_uzun(matn))

# 2 chi
# def saralash(matn:str):
#     with open("function.txt","w") as f:
#         natija=sorted(matn.split())
#         for i in natija:
#             f.write(i+" ")
#     return natija
# print(natija:=saralash("Foydalanuvchidan eng uzun matn kiriting"))

# not finished
# def oqish(fayl:function.txt):
#     with open("function.txt","r") as f:
#         matn=f.read()
#         print(len(matn.split()))
# print(oqish())
# -----------------------------------------------------------------
# 5 chi misol
# def unikal(lst:list):
#     dct={}
#     for i in lst:
#         if i not in dct:
#             dct[i]=lst.count(i)
#     print(dct)
#     for i ,v in dct.items():
#         count=0
#         for x,v2 in dct.items():
#             if v==v2:
#                 count+=1
#         if count!=1:
#             return False
#             break
#         else:
#             return True

# lst=[1,2]
# print(unikal(lst))
# ---------------------------------------------
# 6 chi misol
# word = "skfdhj123kjhsk12sdfhb34hshf"

# for char in word:
#     if not char.isdigit():
#         word = word.replace(char, ' ')
# print(word)

# sonlar_listi = []
# bo_laklar = word.split()

# for num in bo_laklar:
#     butun_son = int(num)
#     sonlar_listi.append(butun_son)
# print(sonlar_listi)

# unikal_sonlar = []

# for son in sonlar_listi:
#     if son not in unikal_sonlar:
#         unikal_sonlar.append(son)

# matn = len(unikal_sonlar)

# print(matn)

# ----------------------------------------
# 7 chi misol
# nums=[6,5,4,8]
# lst=[]

# for i in nums:
#     count=0
#     for x in nums:
#         if i>x:
#             count+=1
#     lst.append(count)
# print(lst)
# -------------------------------
# 8 chi misol
def function(text:str):
    lst=[]
    for i in text:
        if not i.isdigit():
            text.replace(i," ")
    text=text.split()
    new=[]
    for i in text:
        if i.isdigit():
            new.append(int(i))
    if sorted(new)==new:
        return True
    else:
        return False

text="Maktabimizda 4-'a' sinfdagi 17 tadan ortiq o'quvchilar imtixondan 86 balldan yuqori ball oldi"
print(function(text))