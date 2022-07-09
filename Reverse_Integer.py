a=int(input())
b=0
if a<0:
    b=1
    a=a-a-a
r=s=0
while a:
    r=a%10
    s=s*10+r
    a=a//10
if b==1:
    s=s-s-s
    print(s)
else:
    print(s)