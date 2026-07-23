# lst
# 1 chi
# n=int(input("nechta raqam kritasiz"))
# lst=[]
# for i in range(n):
#     lst.append(int(input()))
# print(lst)
# ------------------
# 0 chi not finished
# n=int(input(">>> "))
# lst=[3,5,6,34,78,33,23]
# for i in lst:
# -------------------------
# 4 chi
# lst=[1,1,100,3,4,5,0,0]
# natija=set(lst)
# print(natija)
# -----------------------
# 5 chi 
# lst=[1,2,3,5,6,7]
# new=[]
# for i in range(lst[-1]):
#     new.append(i+1)
# print(new)
# lst=new
# print(lst)
# ---------------------------------
# MOCK
# 1 chi misol
# dct={
#     "yanvar":"01",
#      "fevral": "02",
#      "mart" : "03",
#      "aprel":"04",
#      "may": "05",
#      "iyun" : "06",
#      "iyul":"07",
#      "avgust": "08",
#      "sentyabr" : "09",
#     "oktyabr":"10",
#      "noyabr": "11",
#      "decabr" : "12"

# }
# n="24 mart 2025"
# print(n[2:-4])
# s=n.split()
# print(f"{s[0]}.{dct[s[1]]}.{s[2]}")
# print(f"{n[:2]}.{n[2:-4]}.{n[-2:]}")
# ---------------------------------------
# 2 chi misol
# numbers=[3,7,12,7,5,3,9,12,15,7]
# n=tuple(set(numbers))
# orta=sum(n)/len(n)
# print(orta)
# -----------------------------------
# 3 chi misol
# import json

# product={
#     "olma": 12000,
#     "banan":18000,
#     "shaftoli": 15000,
#     "uzum":20000
# }

# maxsulot=input("maxsulot nomini kriting: ").lower()
# miqdor=int(input("nechta olishingizni kriting: "))

# if maxsulot in product:
#     narx=product[maxsulot]*miqdor

#     data={
#         "maxsulot":maxsulot,
#         "miqdor":miqdor,
#         "narx": narx
#     }
#     print(f"umumiy narx={narx}")

#     with open("dokon.json","w") as file:
#         json.dump(data,file,indent=4)


# else:
#     print("bunday maxsulot mavjut emas.")
# ---------------------------------------------------------------
# 4 chi misol
# lst=input("matn kiriting: ")
# lst=lst.split()
# print(lst)
# uzun=max(lst,key=len)

# print(uzun)
# print(t:=sorted(lst))
# with open("function.txt","w") as f:
#     print(" ".join(t))

import json 

with open("test.json") as f:
    data = json.load(f)
    dct = {"payment":0}
    # for branch in data["branches"]: 
    #     for student in branch['students']:
    #         if dct["payment"] < student['payment']:
    #             dct = student.copy()
    #             dct["branch"] = branch['name']
                # print(branch)
    print(dct)

    lst = []
    for branch in data['branches']:
        lst += branch['students']
    print(max(lst, key=lambda x: x['payment']))



            
        
            



    
