def isprime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
b=1
for i in range(2,a+1):
    if a%i==0:
        if isprime(i)==0:
            b+=1
print(b)