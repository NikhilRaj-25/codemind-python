a=int(input())
b=a
s=r=0
while b:
    r=b%10
    s=s*10+r
    b=b//10
if a==s:
    print('True')
else:
    print('False')