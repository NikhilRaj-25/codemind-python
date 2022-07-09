a=int(input())
l=list(map(int,input().split()))
b=int(input())
c=0
for i in range(a):
    if l[i]==b:
        c=1
        print(i,end=" ")
        break
if c==0:
    print('-1',end=" ") 
d=[]
for i in range(a-1,-1,-1):
    d.append(l[i])
c=0
for i in range(a):
    if d[i]==b:
        c=1
        print(a-i-1,end=" ")
        break
if c==0:
    print('-1',end=" ")