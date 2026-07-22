# 1 chi misol
import json
with open("uyga_vazifa10.json") as f:
    dct=json.load(f)
    new=dct["branches"]
    for i  in new:
        print(i["name"])