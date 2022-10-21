a=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
ans=[]
b=0
for i in range(0,a):
    b=l1[i]+l2[i]
    ans.append(b)
print(*ans)