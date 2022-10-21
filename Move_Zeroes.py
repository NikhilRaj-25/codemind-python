a=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if(i==0):
        c+=1
ans=[]
for i in l:
    if i!=0:
        ans.append(i)
while(c):
    ans.append(0)
    c-=1
print(*ans)