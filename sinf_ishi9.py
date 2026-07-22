import json
# 1 chi masala
# with open("test.json") as f:
#     natija=json.load(f)
#     for i in natija:
#         if "Matematika" in i["subjects"]:
#             print(i)
# --------------------------------------------
# 2 chi masala
# with open("test2.json","r") as f:
#     natija=json.load(f)
#     sum=0
#     for i in natija:
#         sum+=i["narx"]*i["son"]
#     print(sum)
# --------------------------------------
# 3 chi masala
# with open("shahar.json") as f:
#     natija=json.load(f)
#     new=max(natija,key=lambda x: x["aholi"])
#     print(new)
# -----------------------------------------------
# 4 chi masala
# with open("dollar.json")as f:
    # natija=json.load(f)
# 1 chisi
#     for i in natija:
#         if 500<i["price"]<1000 and i["is_available"]==True:
#             print(f"Id raqam->{i["id"]}  material-> {i["material"]}")
# 2 chisi
    # material = input(">> ")
    # lst = []
    # for i in json.load(f):
    #     if material == i['material'] and i['is_available']:
    #         lst.append(i)
    # lst.sort(key=lambda x: x['price'])
    # print(lst)
# 3 chisi
    # for i in json.load(f):
    #     if i["is_available"]==False and i["price"]<1000:
    #         print(i["material"])
    



# ----------------------------------------------------------------------
#  chi masala
# f = open("test5.txt", "w")

# f.write(f"{56+1}")

# lst = [23, 12, 45, -3, 12, 0, -12]
# for i in lst:
#     if i > 0:
#         f.write(f"{i} ")

# lst = ["salom", 'kiyik', "amma", "oftob"]
# for i in lst:
#     if i==i[::-1]:
#         f.write(f"{i} ")

# f.close()
# import json

# f = open("test.json")

# natija = json.load(f)
# print(natija)

# f.close()
# import json 

# with open("test2.json") as f:
#     dct = json.load(f)
#     for i in dct:
#         print(i)
#         for subject in dct[i]:
#             print(f"\t{subject} -> {sum(dct[i][subject])/len(dct[i][subject])}")

# ----------------------------------------------------------------------------
# OSON
# 1 chi misol
# import json
# with open("people.json") as f:
#     dct=json.load(f)
#     for i in dct:
#         for i in dct[i]:
#             print(i["name"])
# ---------------------------------
# 2 chi misol
# with open("user.json") as f:
#     dct=json.load(f)
#     sum=0
#     for i in dct:
#         for i in dct[i]:
#             sum+=i["age"]            
# print(sum)
# ---------------------------------
# 3 chi misol
# with open("products.json") as f:
#     dct=json.load(f)
#     for i in dct:
#         for x in dct[i]:
#             print(f"{x["name"]}: {x["price"]}")
# ------------------------------------
# 4 chi misol
# with open("people.json") as f:
#     dct=json.load(f)
    # max=0
    # for i in dct:
    #     for x in dct[i]:
    #         if max<x["age"]:
    #             max=x["age"]
    # for i in dct:
    #     for x in dct[i]:
    #         if x["age"]==max:
    #                 print(x["name"])
    # ------------------
    # not finished 
    # dct=list(dct)
    # print(dct)
    # print(max(dct,key=lambda x:x["age"] ))
    # ------------------------------------------
# 5 chi masala
# with open("contacts.json") as f:
#     dct=json.load(f)
#     for i in dct:
#         for x in dct[i]:
#             print(x["phone"])
# ----------------------------------------------
# O'rta
# 6 chi misol
# with open("students.json") as f:
#     dct=json.load(f)
#     for i in dct:
#         for x in dct[i]:
#             print(f"{x["name"]}: {sum(x["grades"])/len(x["grades"])}")
# ------------------------------------------------------------------------
# 7 chi masala
# with open("users.json") as f:
#     dct=json.load(f)
#     for i in dct:
#         for x in dct[i]:
#             if x["role"]=="admin":
#                 print(x["name"])
# -------------------------------------
# 8 chi misol
# with open("categories.json") as f:
#     dct=json.load(f)
#     max=0
#     for i,v in dct.items():
#         for a,b in v.items():
#             if max<len(b):
#                 max=len(b)

#     for i,v in dct.items():
#         for a,b in v.items():
#             if max==len(b):
#                 print(a)
# ------------------------------------
# 9 chi misol
# with open("births.json") as f:
#     dct=json.load(f)
#     for i in dct:
#         for x in dct[i]:
#             if x["birth_year"]>1990:
#                 print(x["name"])
# ------------------------------------
# 10 chi misol
# with open("departments.json") as f:
#     dct=json.load(f)
#     for i,v in dct.items():
#         for x,c in dct[i].items():
#             print(f"{x}: {len(c)}")
# ------------------------------------------
# 11 chi misol
# with open("orders.json") as f:
#     dct=json.load(f)
#     new={}
#     for i in dct:
#         for x in dct[i]:
#             if x["customer"] not in new:
#                 new[x["customer"]]=x["amount"]
#             else:
#                 new[x["customer"]]+=x["amount"]
#     for i,v in new.items():
#         print(f"{i}: {v}")
# --------------------------------------------------
# 12 chi misol not finished
# with open("courses.json") as f:
#     for i ,v in json.load(f).items():
#         for type,fan in v.items():
#             sum=0
#             for c in fan:
#                 sum+=c["grade"]
#             print(f"{type} ->{sum/len(fan)}")
# --------------------------------------
# 13 chi misol not finished
# with open("products.json") as f:
#     dct=json.load(f)
#     data=dct["products"]
#     print(data)
#     print(natija:=max(data, key=lambda x: x["price"]))
    # print(f"{natija["name"]}: {natija["price"]}")
# -------------------------------------------------
# 14 chi misol not finished
# with open("sales.json") as f:
#     dct=json.load(f)
#     data=dct["sales"]
#     new={}
#     for i in data:
#         if i["month"] not in new:
#             new[i["month"]]=i["amount"]
#         else:
#             new[i["month"]]+=i["amount"]
#     for i in new:
#         print(f"{i}: {new[i]}")
# --------------------------------------------
# 15 chi misol
# with open("social_users.json") as f:
#     dct=json.load(f)
#     new=[]
#     for i in dct:
#         for x in dct[i]:
#             if len(x["social"])>=2:
#                 new.append(x["name"])
#     print(new)
# -----------------------------------------
# Uyga vazifa
# 1 chi misol
# with open("orders.json") as f:
#     lst=json.load(f)
#     dct={}
#     for i in lst:
#         sum=0
#         for x in i["items"]:
#             sum+=(x["price"]*x["quantity"])
#         dct[i["order_id"]]=sum
#     print(max(dct,key=dct.get))
# ---------------------------------
# 2 chi misol
# with open("menu.json") as f:
#     dct=json.load(f)
#     new={}
#     for i,v in enumerate(dct):
#         if v["category"]=="Pizza":
#             print(v)
    
#     for i in dct:
#         new[i["name"]]=i["price"]
#     print(new)
#     print(f"MAX->{max(new,key=new.get)}")
#     print(f"MIN->{min(new,key=new.get)}")
# ----------------------------------------------
# 3 chi misol
# with open("tickets.json ") as f:
#     lst=json.load(f)
    # for i in lst:
    #     if i["from"]=="Tashkent":
    #         print(i)
    # print(max(lst,key=lambda x:x["price"]))
    # print(min(lst,key=lambda x:x["price"]))
# ---------------------------------------------
# 4 chi misol
# with open("weather.json") as f:
#     lst=json.load(f)
# print(a:=max(lst,key=lambda x:x["temperature"]))
# print(b:=min(lst,key=lambda x:x["temperature"]))
# print(f"O'rtacha harorat->{(a["temperature"]+b["temperature"])/2}")
# -----------------------------------------------
with open("students.json") as f:
    lst=json.load(f)
    python=0
    Java=0
    ml=0
    js=0
    ai=0
    cyber=0
    math=0
    dc=0
    c=0
    
    new=[]
    for i in lst:
        if "Python"in i["courses"]:
            python+=1
    print(f"Python->{python}")
    for i in lst:
        if "Java"in i["courses"]:
            Java+=1
        elif "Python" in i["courses"]:
            python+=1
        elif "Machine Learning" in i["courses"]:
            ml+=1
        elif "Javascript" in i["courses"]:
            js+=1
        elif "Database" in i["courses"]:
            data+=1
        elif "AI" in i["courses"]:
            ai+=1
        elif "Cybersecurity" in i["courses"]:
            cyber+=1
        elif "Math" in i["courses"]:
            math+=1
        elif "Data Science" in i["courses"]:
            ds+=1
        elif "C#" in i["courses"]:
            c+=1
    print(f"Java->{Java}")
        


    


