a=int(input())
sq=a*a
rem=0
s=0
while sq!=0 :
    rem=sq%10
    s=s+rem
    sq=sq//10
if a==s :
    print("Neon Number")
else:
    print("Not Neon Number")