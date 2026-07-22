# 1 chi masala
# def format_date(dct=dict,date=str):
    # for i,v in dct.items():
    #     if i==str(date[3:5]):
    #         print(f"{date[:2]} {v} {date[6:]} yil")
            # second way
        # print(f"{date[:2]} {dct[date[3:5]]} {date[6:]} yil")



# dct={
#     "01":"yanvar",
#     "02":"fevral",
#     "03":"mart",
#     "04":"aprel",
#     "05":"may",
#     "06":"iyun",
#     "07":"iyul",
#     "08":"avgust",
#     "09":"sentabr",
#     "10":"oktabr",
#     "11":"noyabr",
#     "12":"dekabr",
# }

# format_date(dct,"01.01.2000")
# ----------------------------------------------------------------------
# 2 chi masala
# def get_top_user(data=list[tuple[str,int]]):
#     print(max(data,key=lambda x:sum(x[1:])))

# data=[
#     ("user1",50),
#     ("user2",80),
#     ("user3",90),
#     ("user4",40,90),
# ]

# get_top_user(data)
# -----------------------------------------------------
# 3 chi masala
# def count_passing_students(grades=list[int],pg=int):
#     count=0
#     for i in grades:
#         if i<=pg:
#             count+=1
#     return count

# grades=[45,60,75,30,90]
# pg=60
# print(natija:=count_passing_students(grades,pg))
# -------------------------------------------------------------
# 4 chi masala
# def ends_with_gram(words=list[str]):
#     new=[]
#     for i in words:
#         if "gram" in i:
#             new.append(i)
#     return new

# words=["telegram","instagram","hello","program","diagram","world"]
# print(natija:=ends_with_gram(words))
