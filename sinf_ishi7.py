# 1 chi masala
# text="Python is great and Python is fun.Learning Python is a great challenge"
# text=text.replace("."," ")

# text=text.split()
# dis={}
# new=[]
# for i in text:




# for i in text:
#     if i in dis:
#         dis[i]+=1
#     else:
#         dis[i]=1
# print(dis)



    #  count=0
    #  for i in text:
    #     print(i)
    #     if i==i:
    #         count+=1
    #  print(f"{i}:{count}")
     
# text=list(set(text))
# print(text)

# --------------------------------------------
# 
# import random

# def Third(l1:list[str], l2:list[str]) -> list:
#     result = [3, 3]
#     for i in range(len(l1)):
#         if l1[i] == "share":
#             result[0] -= 1
#             result[1] += 3
        
#         if l2[i] == "share":
#             result[1] -= 1
#             result[0] += 3
#     return result


# aziz = ["share", "steal", "share"]
# karim = ["steal", "steal", "steal"]

# natija = Third(aziz, karim)
# print(natija)


# def Third() -> list:
#     lst = [3, 3]
#     for i in range(int(input(">>> "))):
#         if "share" == random.choice(["share", "steal","gain"]):
#             lst[0] -= 1
#             lst[1] += 3
        
#         if "share" == random.choice(["share", "steal","gain"]):
#             lst[1] -= 1
#             lst[0] += 3
#     return lst

# natija = Third()
# print(natija)

# natija = list(filter(lambda x: len(x)>5, ["salom", "malina", "foundation"]))
# natija = list(filter(lambda x: x, [45, 32, 0, 12 ,33]))
# natija = list(filter(lambda x: x%2, [45, 32, 0, 12 ,33]))
# natija = list(filter(lambda x: x==x[::-1], ["amma", "uka", "ada", "kiyik"]))

# # natija = [i for i in ["salom", "malina", "foundation"] if len(i)>5]

# natija = list(map(lambda x: x**2, [2,5,1,2]))
# natija = list(map(lambda x: x%2==0, [45, 32, 0, 12 ,33]))

# print(natija)

# -------------------------------------------------------------
# data = "Python is great and Python is fun. Learning Python is a great experience"

# dct = {}

# for i in data.split():
#     print(i, data.count(i))
#     # dct[i] = data.count(i)
#     if i not in dct:
#         dct[i] = 1
#     else:
#         dct[i] += 1

# print(dct)
# -------------------------------------
# Notion
# 1 chi masala
# str="13.09.2025"


# dct={"01":"yanvar","02":"fevral","03":"mart","04":"aprel",
#      "05":"may","06":"iyun","07":"iyul","08":"avgust",
#      "09":"sentabr","10":"oktabr","11":"noyabr","12":"dekabir"}
# for i , q in dct.items():
#     if str[3:5]==i:
#         print(f"{str[:2]} {q} {str[6:]} yil")

# print(f"{str[:2]} {dct[str[3:5]]} {str[6:]} yil")

# def function(n):
#     dct={
#         1:"Dushanba",
#         2:"seshaba",
#         3:"chorshanba",
#         4:"payshanba",
#         5:"juma",
#         6:"shanba",
#         7:"yakshanba"
#     }

#     return dct[n]

# print(function(6))

# -------------------------------------------------
# 2 chi masala
# def get_top_user(data=list[tuple[str,int]]):
#     return max(data,key=lambda x:sum(x[1:]))


# data=[
#     ("user1",50,50),
#     ("user2",60),
#     ("user3",40),
#     ("user4",30),
# ]

# natija=get_top_user(data)
# print(natija)
# ---------------------------------------
# 2 chi masala
lst=["Ali, ali@gmail.com", "Vali, vali123@mail.ru", "Aziza, aziza@outlook.com"]


new=[]
for i in lst:
        print(i)
        new.append(i[1])
print(new)














