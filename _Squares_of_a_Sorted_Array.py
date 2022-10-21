a=int(input())
l=list(map(int,input().split()))
ans=[]
b=0
for i in range(0,a):
    b=l[i]*l[i]
    ans.append(b)
ans.sort()
print(*ans)