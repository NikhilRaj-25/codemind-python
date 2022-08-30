i=1
count=0
a=int(input())
b=int(input())
c=a+b
while i<=c:
    d=c+i
    count+=1
    sum=0
    for j in range(1,d+1):
        if d%j==0:
            sum+=1
    if sum==2:
        print(count)
        break
    i+=1