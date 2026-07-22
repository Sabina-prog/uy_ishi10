# 1 chi misol
# lst=[3,89,7,False]
# max=0
# min=0

# for i in lst:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
    
# print(max)
# print(min)
# --------------------------
# 1 chi misol
# lst=[True,"Salom",5,5.6]

# for i in lst:
#     print(type(i))
# -------------------------------
# 2 chi misol
# lst=[7,8,1,3,4,6,7,5]
# lst2=lst.copy()

# for index,value in enumerate(lst):
#     if index%2:
#         lst2[index]=(value*value*value)
#     else:
#         lst2[index]=(value*value)
# print(lst2)
# ------------------------------------
# 3 chi misol
# llst = [34, 12, 10]
# natija = lst.pop()
# print(lst)
# print(natija)



# lst = [[1,2,3,4], [1,2,3], [6,1], [1,9]]
# new = []

# for i in lst:
#     new.append(sum(i))

# print(new)

# lst = [34, 12, 10]
# natija = lst.pop()
# print(lst)
# print(natija)

# lst = [34, 12, 54, 23]
# lst.sort()
# lst.reverse()
# lst.sort(reverse=True)
# print(lst)
lst = [[1,4,3], [4,2,6,2], [0,-1,45]]

for index, value in enumerate(lst):
    if index%2:
        value.sort(reverse=True)
    else:
        value.sort()

print(lst)



