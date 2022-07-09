a=int(input())
l=list(map(int,input().split()))
if a%2==0:
    for i in range((a//2)):
        print(l[i],end=" ")
        print(l[a-i-1],end=" ")
else:
    for i in range((a//2)):
        print(l[i],end=" ")
        print(l[a-i-1],end=" ")
    print(l[(a//2)],end=" ")
if a%2!=0:
    print('0')