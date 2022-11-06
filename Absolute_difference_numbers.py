a,b=map(int,input().split())
c=pow(10,b)
d=a%c
s=r=0
while a!=0:
    r=a%10
    s=s*10+r
    a=a//10
f=s%c
s=r=0
while f!=0:
    r=f%10
    s=s*10+r
    f=f//10
print(abs(d-s))