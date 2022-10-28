a=input()
l=a.split()
v="aeiou"
d=999
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    if d>c:
        d=c
print(d)