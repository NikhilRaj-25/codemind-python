n=int(input())
max=-100
arr=list(map(int,input().split()))
for i in arr:
    if i>max:
        max=i
while(True):
    t=0
    for i in range(n):
        if max%arr[i]==0:
            t+=1
    if t==n:
        print(max)
        break
    else:
        max+=1