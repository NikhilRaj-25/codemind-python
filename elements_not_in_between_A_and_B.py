a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
for i in l:
    if i>=b and i<=c:
        continue
    else:
        d=1
        print(i,end=" ")
if d==0:
    print('-1')