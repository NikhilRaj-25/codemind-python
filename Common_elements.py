a,b=map(int,input().split())
l=list(map(int,input().split()))
ls=list(map(int,input().split()))
d=[]
for i in l:
    if i not in d:
        d.append(i)
c=[]
for i in d:
    if i in ls:
        c.append(i)
print(*c)