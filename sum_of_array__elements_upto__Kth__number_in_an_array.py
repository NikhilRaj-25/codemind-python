a=int(input())
l=list(map(int,input().split()))
b=int(input())
s=0
for i in l:
    if i!=b:
       s+=i
    else:
        s+=i
        break
print(s)