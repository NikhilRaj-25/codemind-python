def s(a):
    summ=0
    for i in range(1,a):
        if a%i==0:
            summ+=i
    return summ
a=int(input())
b=int(input())
c=s(a)
d=s(b)
if a==d and b==c:
    print('Amicable')
else:
    print('Not Amicable')