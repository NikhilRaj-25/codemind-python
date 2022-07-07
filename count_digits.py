a=int(input())
lst=list(map(int,input().split()))
b=[]
for i in lst:
    c=0
    if i<0:
        i=i-i-i
    if i==0:
        b.append(1)
    else:
        while i:
            i=i//10
            c+=1
        b.append(c)
print(*b)