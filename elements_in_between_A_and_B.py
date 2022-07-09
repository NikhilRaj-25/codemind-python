n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
ans=[]
c=0
for i in arr:
    if i>=a and i<=b:
        c=1
        ans.append(i)
if c==1:
    print(*ans)
else:
    print('-1')