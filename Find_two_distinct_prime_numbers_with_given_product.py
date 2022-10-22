def isprime(a):
    if a<2:
        return 0
    else:
        for i in range(2,(a//2)+1):
            if a%i==0:
                return 0
        return 1
    
a=int(input())
l=[]
for i in range(2,a):
    if a%i==0 :
        l.append(i)
b=len(l)
c=0
for i in range(0,b):
    if isprime(l[i]):
        if(isprime(l[b-1-i])):
            print(l[i],end=" ")
            print(l[b-1-i])
            c=1
            break
if c==0:
    print('-1')