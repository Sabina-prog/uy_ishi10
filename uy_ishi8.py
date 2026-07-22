f=open("moshina.txt")
lst=f.read().split("\n")
new=[]
for i in lst:
    new.append(i.split(",")[4])
st=set(new)
dct={}
lst2=[]
dct2={}

for i in st:
    dct[i]=new.count(i)

print(natija:=max(dct.items(),key=lambda x:x[1]))

for i in lst:
    if natija[0] in i:
        lst2.append(i.split(",")[-1])

st2=set(lst2)

for i in st2:
    dct2[i]=lst2.count(i)

print(f"MAX>>>>>> {max(dct2.items(),key=lambda x: x[1])}")
print(f"MIN>>>>>> {min(dct2.items(),key=lambda x: x[1])}")