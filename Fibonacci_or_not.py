a=int(input())
b=d=0
c=1
while d<a:
    d=b+c
    b=c
    c=d
if d==a:
    print('True')
else:
    print('False')