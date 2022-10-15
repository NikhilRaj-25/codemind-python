a=int(input())
l=[]
for i in range(0,a):
    c=int(input())
    l.append(c)
b=int(input())
ans=0
for i in l:
    if i>b:
        ans+=2
    else:
        ans+=1
print(ans)