a=int(input())
lst=list(map(int,input().split()))
ans=[]
for i in lst:
    b=0
    for j in lst:
        if i>j:
            b+=1
    ans.append(b)
print(*ans)