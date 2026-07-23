# 1 chi misol
import json
with open("uyga_vazifa10.json") as f:
    dct=json.load(f)
    # new=dct["branches"]
    # for i  in new:
    #     print(i["name"])
# --------------------------------------------
# 2 chi misol
    # for i in dct["branches"]:
    #     for x in i["teachers"]:
    #         if x["subject"]=="Python":
    #             print(x["name"],i["name"],x["experience"],x["subject"])
# ---------------------------------------------------------------
# 3 chi misol
    # for i in dct["branches"]:
    #     count=0
    #     for x in i["students"]:
    #         count+=1
    #     print(i["name"],count)
# -----------------------------------------------------------
# 4 chi misol
# for i in dct["branches"]:
#     a={"payment":0}
#     for x in i["students"]:
#         if x["payment"]>a["payment"]:
#             a=x.copy()
#             a["branch"]=i["name"]
# print(a["name"],a["branch"])
# -------------------------------------------
# 5 chi misol
    # for i in dct["branches"]:
    #     sum=0
    #     for x in i["students"]:
    #         sum+=x["payment"]
    #     print(i["name"],sum)
# -------------------------------------
# 6 chi misol
    # for i in dct["branches"]:
    #     for x in i["teachers"]:
    #         if x["experience"]>5:
    #             print(x["name"],x["experience"])
# -----------------------------------------------------
# 7 chi misol
    # for i in dct["branches"]:
    #     for x in i["teachers"]:
    #         if x["subject"]!="Python":
    #             break
    #     else:
    #         print(i["name"])