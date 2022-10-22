num=int(input())
a=0
b=1
c=0
while(c<num):
    c=a+b;
    a=b;
    b=c;
if num-a == b-num:
    print(a,end=" ")
    print(b)
elif num-a > b-num:
    print(b)
else:
    print(a)