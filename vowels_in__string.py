a=input()
ans=0
v="aeiouAEIOU"
c=[]
for i in a:
    if (i in v) and (i not in c):
        c.append(i)
if len(c)>0:
    ans=1
    print(*c)
if ans==0:
    print('-1')