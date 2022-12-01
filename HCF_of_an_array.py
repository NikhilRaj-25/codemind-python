n=int(input())
arr=list(map(int,input().split()))
m=min(arr)
while m>0:
    count=0
    for i in arr:
        if i%m==0:
            count+=1
    if count==n:
        print(m)
        break
    else:
        m-=1