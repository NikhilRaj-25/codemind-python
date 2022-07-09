a=int(input())
l=list(map(int,input().split()))
for i in range((a//2)):
    print(l[i],end=" ")
    print(l[a-i-1],end=" ")
if a%2!=0:
    print(l[(a//2)],end=" ")
    print('0')