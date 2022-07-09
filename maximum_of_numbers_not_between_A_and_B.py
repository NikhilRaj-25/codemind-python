a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
e=[]
for i in l:
    if i>=b and i<=c:
        continue
    else:
        d=1
        e.append(i)
if d==0:
    print('-1')
else:
    print(max(e))