a=int(input())
b=a
l=[]
s=r=c=0
while b!=0:
    c+=1
    r=b%10
    b=b//10
    l.append(r)
l1=len(l)
for i in range(l1-1,-1,-1):
    if l[i]==6:
        l[i]=9
        break
for i in range(l1-1,-1,-1):
    print(l[i],end="")