a=int(input())
lst1=list(map(int,input().split()))
b=int(input())
lst2=list(map(int,input().split()))
c=int(input())
count=0
for i in range(a):
    if lst1[i]<c and lst2[i]>c:
       count+=1
    elif lst1[i]==c or lst2[i]==c:
         count+=1
print(count)