a=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
avg=float(s/a)
b=co=0
for i in l:
    if avg-1<i:
        co+=1
print(co)