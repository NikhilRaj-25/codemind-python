a=input()
l=a.split()
b=""
for i in range(len(l)-1,-1,-1):
    b=l[i]
    print(b[::-1],end=" ")