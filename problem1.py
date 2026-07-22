# def check_anagram(a:str,b:str):
#     for i in b:
#         if i.lower() in a.lower():
#             return True
#         else:
#             return False
    
# natija=check_anagram("Listen","silent")
# print(natija)
# --------------------------------------------
# 2 chi misol
# def numbers(numbers:list)->list:
#     lst=[]
#     for i in numbers:
#         yangi=""
#         for x in i:
#             yangi_raqam=(int(x)+3)%10
#             yangi+=str(yangi_raqam)
#         lst.append(yangi)
#     return lst


# raqamlar=[
#     "37412",
#     "9999",
#     "12345",
#     "0000",
#     "56789"
# ]

# print(natija:=numbers(raqamlar))

# def nima(number:list)->list:
#     shifr=[]

#     for satr in number:
#         yangi=""
#         for i in satr:
#             yangi_raqam=(int(i)+3)%10 

#             yangi+=str(yangi_raqam)

#         shifr.append(yangi)
#     return shifr

# # lst=["1111","2222","9999"]
# raqamlar=["37412","9999","12345","0000","56789"]
# print(nima(raqamlar))
