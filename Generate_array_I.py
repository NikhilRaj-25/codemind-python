a=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l),2):
    for j in range(0,l[i+1]):
        print(l[i],end=" ")