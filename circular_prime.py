def p(a):
    b=0
    for i in range(2,(a//2)+1):
        if a%i==0:
            b=1
            break
    if b==0:
        return 1
    else:
        return 0
a=int(input())
b=r=0
s=a
while s:
    r=s%10
    b=b*10+r
    s=s//10
if p(a)==1 and p(b)==1:
    print('circular prime')
elif p(a)==1 and p(b)==0:
    print('prime but not a circular prime')
else:
    print('not prime')