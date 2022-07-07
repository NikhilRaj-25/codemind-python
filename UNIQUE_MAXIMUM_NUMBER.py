a=int(input())
lst=list(map(int,input().split()))
b=0
c=0
for i in lst:
    if lst.count(i)==1:
        c=1
        if i>b:
            b=i
if c==1:
    print(b)
else:
    print('-1')