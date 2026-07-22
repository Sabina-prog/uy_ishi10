# 1 chi masala
def function(a:list):
    dct={}
    for i in a:
        dct[i]=a.count(i)
    return dct

# 2 chi masala
def Uzgargan_son(k:int,n:int):
    return int(str(k)+str(n))




# 2 chi masala
# natija=Uzgargan_son(9,6532)
# print(natija)



# 1 chi masala
# natija=function("w3resource")
# # for i in "w3resource":
# print(natija)

# 3 chi masala
# def alpha(a:str):
#        for i in a.split:
#             print(i)
            
            
#        return a.replace(a[0][0],a[-1][-1])

# print(natija:=alpha("London is the capital of great Britain"))

# 4 chi masala
# def two(d1:dict,d2:dict):
#     for i,v in d1.items():
#         if i in d2:
#             d2[i]=d1[i]+d2[i]
#         else:
#             d2[i] = v
#     return d2

# print(natija:=two({"a":100,"b":200,"c":300},{"a":300,"b":200,"d":400}))

# 5 chi masala
# a = {"A":100, "B":200, "C":50}
# b = {"D":12, "E":11, "F":12}
# c = {"G":47, "H":17}
# new = {}
# new.update(a)
# new.update(b)
# new.update(c)
# new.update([(1,1),(2,21),(3,12)])

# print(new)

# groups = {
#     211 : {
#         "soni" : 12,
#         "students" : {
#             "Behruz" : 70,
#             "Javohir" : 70,
#             "Asilbek" : 70
#         }
#     },
#     212 : {
#         "soni" : 16,
#         "students" : {
#             "Jahongir" : 95,
#             "Lobar" : 60,
#             "Sabina" : 100
#         }
#     },
#     219 : {
#         "soni" : 16,
#         "students" : {
#             "Alixon" : 56,
#             "Umid" : 70,
#             "Abror" : 67
#         }
#     },
#     216 : {
#         "soni" : 14,
#         "students" : {
#             "Elbek" : 100,
#             "MuhammadZiyo": 90,
#             "Suhrob": 77
#         }
#     }
# }

# # print(groups[216]['students']['MuhammadZiyo'])
# for i in groups:
# #     print(i, max(groups[i]['students'].items(), key=lambda x: x[1]))
# #     print(groups[i]['students'].items())



# lst = [23,12,34,54,12,23,12]
# print(lst:=set(lst))
# print(lst)

# st = {"Apple", "Microsoft", "Apple", "Uber", "Yandex", "Netflix"}




# for i in st.copy():
#     if len(i) > 5:
#         st.remove(i)
# print(st)


# print(st)
# st.pop()
# print(st)
# st.pop()
# print(st)
# st.pop()
# print(st)


# st.add(input(">>> "))
# print(st)

# st.update([12, 23, 4], [22, 12, 4])
# print(st)

# a = ["Olma", "Karam", "Qovun"]
# b = ["Uzum", "Olma", "Nok"]
# c = ["Shaftoli", "Limon", "Qovun", "Olma"]

# for i in a.copy():
#     if i in b or i in c:
#         a.remove(i)
# print(a)

# a = list(set(a).difference(b, c))
# print(a)

# natija = set(a).intersection(b, c)
# print(natija)

# natija = set(a).symmetric_difference(b)
# print(natija)

# def test(a:int, b:int):
#     return a+b

# def Yil(sana:str):
#     return sana[-4:]

# def Chopish(a:list[str]) -> None:
#     for i in a:
#         if i == i[::-1]:
#             print(i)

# def Katta(a, b, c, d=12):
#     return max(a, b, c, d)

# natija = Yil("12.12.2020")
# print(natija)

# Chopish(["salom", "kiyik", "amma", "malina"])

# natija = Katta(3, 1, 2)
# print(natija)

def Uchinchi(a: str):
    lst = []
    for i in a.split():
        lst.append(i[-1]+i[1:-1]+i[0])
    return " ".join(lst)

matn = input()
natija = Uchinchi(matn)
print(natija)

