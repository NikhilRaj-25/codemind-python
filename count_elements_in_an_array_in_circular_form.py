a=int(input())
l=list(map(int,input().split()))
b=[]
b.append(l[a-2])
b.append(l[a-1])
c=0
for i in l:
    b.append(i)
for i in range(a):
    if b[i]%2==0 and b[i+2]%2!=0:
        c+=1
    elif b[i]%2!=0 and b[i+2]%2==0:
        c+=1
print(c)