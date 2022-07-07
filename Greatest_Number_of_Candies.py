a=int(input())
lst=list(map(int,input().split()))
b=int(input())
c=0
for i in lst:
    d=0
    c=i+b
    for j in lst:
        if c>=j:
            d+=1
    if d==a:
        print('True',end=" ")
    else:
        print('False',end=" ")