a=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    b=0
    while i:
        i=i//10
        b+=1
    if b%2==0:
        c+=1
print(c)