a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
ans=0
for i in l:
    if i>=b and i<=c:
        ans+=i
print(ans)