a=input()
l=a.split()
c=0
v="aeiouAEIOU"
for i in l:
    b=len(i)
    if (i[0] in v) and (i[b-1] not in v):
        c+=1
print(c)