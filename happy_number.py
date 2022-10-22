a=int(input())
s=0
while a>9:
    s=s1=r=0
    b=a
    while b:
        r=b%10
        s1=r*r
        s+=s1
        b=b//10
    a=s
if s==1 or s==7:
    print('True')
else:
    print('False')