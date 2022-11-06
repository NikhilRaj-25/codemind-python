def fact(a):
    if a<=1:
        return 1
    else:
        return a*fact(a-1)
a=int(input())
b=a
s=r=0
while b!=0:
    r=b%10
    s+=fact(r)
    b=b//10
if s==a:
    print('The number',a,'is a strong number')
else:
    print('The number',a,'is not a strong number')