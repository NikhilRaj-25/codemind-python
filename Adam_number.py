a=int(input())
sq=a*a
b=a
rem=0
su=0
while b!=0:
    rem=b%10
    su=su*10+rem
    b=b//10
sq1=su*su
c=sq1
su=0
rem=0
while c!=0:
    rem=c%10
    su=su*10+rem
    c=c//10
if su==sq:
    print("True")
else :
    print("False")