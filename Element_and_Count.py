a=int(input())
l=list(map(int,input().split()))
l1=[]
ans=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    ans.append(i)
    ans.append(l.count(i))
print(*ans)