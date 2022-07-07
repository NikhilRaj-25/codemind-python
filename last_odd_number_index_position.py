a=int(input())
l=list(map(int,input().split()))
o=0
for i in range(a):
    if l[i]%2!=0:
        o=i
print(o)