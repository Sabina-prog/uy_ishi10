# 1 chi masala
# keys=["Ten","Twenty","Thirty"]
# values=[10,20,30]
# dct={}

# for i in range(len(keys)):
#     dct[keys[i]]=values[i]
# print(dct)
# -----------------------------------
# 2 chi masala
# dct={"a":100,
#      "b":200,
#      "c":300}

# if 200 in dct.values():
#     print("bor")
# else:
#     print("yo'q")
# ---------------------------------
# 3 chi masala
# dct={1:10,2:20,3:30,4:55,5:25}

# dct.pop(max(dct,key=lambda x: dct[x]))
# dct.pop(min(dct,key=lambda x: dct[x]))

# print(dct)
# ---------------------------------------------
# 4 chi masala
# dct1={1:10,2:20}
# dct2={3:30,4:40}
# dct3={9:90,7:70}


# print(all)
### 4
# dct1 = {1: 10, 2: 20}
# dct2 = {3: 30, 4: 40}
# dct3 = {5: 50, 6: 60}
# dct = {}
# for v in dct1:
#     dct[v] = dct1[v]
# for v in dct2:
#     dct[v] = dct2[v]
# for v in dct3:
#     dct[v] = dct3[v]
# print(dct)
# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# for index, value in enumerate(lst):
#     print(index)
#     value = list(value)
#     value[-1] = 100 
#     lst[index] = tuple(value)
# print(lst)

# lst = [1, 2, 33, 5, 6, 7, 7]
# n = 9

# for index, value in enumerate(lst):
#     for index2, value2 in enumerate(lst[index+1: ]):
#        if value + value2 == n:
#            print(f"{index} - {index2+1+index}")

# lst = [1, 2, 3, 4]
# prefix = "emp"
# natija = [prefix+str(i) for i in lst]
# print(natija)


# student = {
#     'ism' : "Sarvar",
#     "age" : 45,
#     "score": 100
# }

# for i in student:
#     print(student[i])
    # if type(student[i]) == int:
    #     print(i, student[i])

# student = {
#     'ism' : "Sarvar",
#     "age" : 45,
#     "score": 100
# }

# for i in student:
#     if type(student[i]) == int:
#         print(i, student[i])


# c=student.pop("age")
# print(c)
# print(student)

# student = {
#     'ism' : "Sarvar",
#     "age" : 45,
#     "score": 100
# }

# for i in student:
#     if type(student[i]) == int:
#         print(i, student[i])


# student.pop("age")
# print(student)

# student['yosh'] = student.pop("age")
# print(student)


# dct = {
#     "A" : 20,
#     "B" : 22,
#     "V" : 15,
#     "C" : 21
# }

# print(sorted(dct))
# print(sorted(dct, key=lambda x: dct[x]))
# print(sorted(dct, key=dct.get))
# print(sorted(dct.items(), key=lambda x: x[1]))

# print(dct.items())
# print(dct.keys())
# print(dct.values())
# print(dct.items())


# dct = {}

# while True:
#     soz = input(">>> ")

#     if soz == "stop":
#         break
#     elif soz not in dct:
#         dct[soz] = 1
#     else:
#         dct[soz] += 1
# print(dct)


# dct = {
#     "house" : 'uy'
# }

# for i in range(int(input("Nechta so'z kiritasiz: "))):
#     english = input("Eng: ")
#     if english in dct:
#         print("Bu so'z band")
#     else:
#         uzbek = input("Uzb: ")
#         dct[english] = uzbek

# print(dct)


### 4
# dct1 = {1: 10, 2: 20}
# dct2 = {3: 30, 4: 40}
# dct3 = {5: 50, 6: 60}
# dct = {}
# for v in dct1:
#     dct[v] = dct1[v]
# for c in dct2:
#     dct[c] = dct2[c]
# for b in dct3:
#     dct[b] = dct3[b]
# print(dct)
# -------------------------------------
# 5 chi masala
# data={"fata1":100,
#       "data2":-54,
#       "data3":245}
    
# print(sum(data.values()))
# 6 chi masala
# data=sorted(data)
# print(data)
# -------------------------------
# 7 chi masala
# data=sorted(data.values())
# print(data)
# -----------------------------------------
# ------------------------------------------
# ------------------------------------------
# 1 chi masala
grades = {
    "Ali": 85,
    "Vali": 78,
    "Hasan": 90
}

c=input("talaba ismi: ")
if c not in grades:
    print("Bunday talaba yo'q")
else:
    c=int(input("yangi bahoni kiritng: "))






