a=int(input())
b=a
rem=0
sum=0
while(a!=0):
    rem=a%10
    sum+=rem
    a=a//10
if b%sum==0:
    print("True")
else:
    print("False")