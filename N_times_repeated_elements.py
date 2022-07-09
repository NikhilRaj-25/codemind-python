a=int(input())
l=list(map(int,input().split()))
b=int(input())
c=[]
d=[]
e=0
for i in l:
    if i not in d:
        d.append(i)
for i in d:
    if b==l.count(i):
        e=1
        c.append(i)
if e==0:
    print('-1')
else:
    print(*c)