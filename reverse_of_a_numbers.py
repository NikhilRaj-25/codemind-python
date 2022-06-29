a=int(input())
s=r=0
while a:
    r=a%10
    s=s*10+r
    a=a//10
print(s)