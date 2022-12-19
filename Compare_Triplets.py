l=list(map(int,input().split()))
l1=list(map(int,input().split()))
a=b=0
for i in range(len(l)):
    if l[i]>l1[i]:
        a+=1
    elif l[i]<l1[i]:
        b+=1
print(a,b)