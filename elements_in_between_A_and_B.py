a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
ans=[]
co=0
for i in l:
    if i>=b and i<=c:
        ans.append(i)
        co+=1
if co==0:
    print(-1)
else:
    print(*ans)