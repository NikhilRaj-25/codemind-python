a,b=map(int,input().split())
l=list(map(int,input().split()))
ls=list(map(int,input().split()))
c=set(l)
d=set(ls)
e=0
for i in c:
    if i not in d:
        e+=1
for i in d:
    if i not in c:
        e+=1
print(e)