a=int(input())
l=list(map(int,input().split()))
b=[]
c=[]
for i in l:
    if i not in c:
        c.append(i)
d=0
for i in c:
    if i==l.count(i):
        d=1
        b.append(i)
if d==0:
    print('-1')
else:
    print(*b)