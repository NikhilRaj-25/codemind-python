n=int(input())
pro=1
s=0
while n!=0 :
    a=n%10
    pro=pro*a
    s=s+a
    n=n//10
print(pro-s)