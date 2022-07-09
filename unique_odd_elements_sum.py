a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b:
        b.append(i)
e=0
for i in b:
    if i%2!=0:
        e+=i
print(e)