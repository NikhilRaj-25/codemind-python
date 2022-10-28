a=input()
l=a.split()
b=""
for i in range(0,len(l)):
    b=l[i]
    if i%2==0:
        print(b[::-1],end=" ")
    else:
        print(b,end=" ")