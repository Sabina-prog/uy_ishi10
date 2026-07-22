import json
with open("oyin.json") as f:
    dct=json.load(f)
    dct=sorted(dct,key=lambda x:x["score"])
    print(dct)
    dct.pop(-1)
    print(dct)
with open("oyin.json","w") as f:
    json.dump(dct,f,indent=4)
    for i in dct[:3]:
        print(i)