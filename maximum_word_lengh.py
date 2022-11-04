a=input()
l=a.split()
c=co=0
for i in l:
    c=0
    for j in i:
        c+=1
    if co<c:
        co=c
print(co)