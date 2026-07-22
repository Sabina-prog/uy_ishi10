# 7 chi masala
# def Half(a:int,b:int):
#     count=0
#     while a>=b:
#         if a%2==0:
#             count+=1
#         a-=1
#     print(count)

# Half(a=int(input("a ni kiriting: ")),b=int(input("b ni kiriting: ")))

# -----------------------------------------------------------------------
# 1 chi masala
# def bigger_price(son:int,lst=list[dict]):
#     for i in son:
#         a=lst.pop(max(lst,key=lambda x:x[price]))

# bigger_price(son=2,lst=[{"name":"bread","price":100},
#                     {"name":"wine","price":138},
#                     {"name":"meat","price":15},
#                     {"name":"water","price":1}])
# ------------------------------------------------------------
# 6 chi masala
# ------------------------------------------------

# def function(d1=dict,d2=dict):
#     new={}
    
# -----------------------------------------
# def function(email=set):

#     return set(email[4:])

# natija=function(email={"user@gmail.com","user2@gmail.ru","user3@gmail.com"})
# print(natija)

# --------------------------------------
# st=["Math","Physics","Math","Biology","Math","Physics"]
# # print(set(st))
# natija=st.intersection(st,st)
# print(natija)

# -----------------------
# 2 chi masala
# lst=["Ali,ali@gmail.com","Vali,vali123@mail.ru","Aziza,aziza@outlook.com"]
# new=[]
# for i in lst:
#     if ","in i:
#         print(i)

# lst=[("Burger", False), ("Salad", True), ("Soup", True), ("Steak", False)]
# new=[]
# for i in lst:
#     if i[1]==True:
#         new.append(i[0])
# print(new)

lst=[55, 60, 75, 90, 45]
natija=[]

natija.append(filter(lambda x:60<=x,lst))
print(natija)
