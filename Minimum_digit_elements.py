a=int(input())
l=list(map(int,input().split()))
b=10
co=0
for i in l:
    c=0
    while i:
       c+=1
       i=i//10
    if c<b:
        b=c
for i in l:
    c=0
    while i:
       c+=1
       i=i//10
    if b==c:
        co+=1
print(co)