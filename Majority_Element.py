a=int(input())
b=a//2
lst=list(map(int,input().split()))
for i in lst:
    if lst.count(i)>b:
        print(i)
        break
