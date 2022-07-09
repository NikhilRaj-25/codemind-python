a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
d=s=0
for i in l:
    if i>=b and i<=c:
        continue
    else:
        d=1
        s+=i
if d==0:
    print('0')
else:
    print(s)