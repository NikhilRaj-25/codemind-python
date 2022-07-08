a,b=map(int,input().split())
l=list(map(int,input().split()))
ls=list(map(int,input().split()))
ans=[]
for i in l:
    if i not in ls:
        ans.append(i)
for i in ls:
    if i not in l:
        ans.append(i)
print(*ans)