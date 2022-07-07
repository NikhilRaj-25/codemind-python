a=int(input())
l=list(map(int,input().split()))
s=c=0
for i in l:
    s+=i
avg=s//a
for i in l:
    if avg+1>i:
        c+=1
print(c)