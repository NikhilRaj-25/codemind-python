a=int(input())
i=1
j=0
b=0
while b<=a:
    b=pow(2,i)
    c=pow(2,j)
    i+=1
    j+=1
d=e=0
d=int(b)
e=int(c)
if((d-a)<(a-e)):
    print(d-a)
else:
    print(a-e)