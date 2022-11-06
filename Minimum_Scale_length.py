a=int(input())
l=list(map(int,input().split()))
m=min(l)
le=len(l)
c=0
i=0
while(True):
    if l[i]%m==0:
        i+=1
        c+=1
    else:
        m-=1
        i=0
        c=0
    if c==le:
        break
print(m)