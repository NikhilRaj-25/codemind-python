a=int(input())
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
    if lst.count(lst[i])>1:
        print(lst[i])
        break