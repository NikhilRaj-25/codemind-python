a=int(input())
l=list(map(int,input().split()))
c=len(l)-1
c1=0
ans=[]
for i in range(len(l)):
    if i%2!=0:
        ans.append(l[c])
        c-=1
    else:
        ans.append(l[c1])
        c1+=1
if a%2!=0:
    ans.append(0)
print(*ans)