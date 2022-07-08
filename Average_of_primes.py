def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
l=list(map(int,input().split()))
s=c=0
for i in l:
    if i>1:
        if prime(i):
            s+=i
            c+=1
avg=float(s/c)
print('%.2f' %avg)