a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
min=l[a-1]
ans=0
for i in l:
    if i>=b and i<=c:
        if i<min:
            min=i
            ans+=1
if ans==0:
    print(-1)
else:
    print(min)
    