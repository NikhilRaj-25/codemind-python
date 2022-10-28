a=input()
l=a.split()
v="aeiou"
d=0
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    print(c,end=" ")