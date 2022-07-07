a=int(input())
lst=list(map(int,input().split()))
b=0
count=0
for i in lst:
    r=s=0
    b=i
    while b:
        r=b%10
        s=s*10+r
        b=b//10
    if s==i:
        count+=1
print(count)