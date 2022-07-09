a=int(input())
l=list(map(int,input().split()))
for i in range(a//2):
    print(l[a-i-1],end=" ")
for i in range(a//2):
    print(l[i],end=" ")