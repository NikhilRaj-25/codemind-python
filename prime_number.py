a=int(input())
b=0
for i in range(2,(a//2)+1):
    if(a%i==0):
        b=1
        break
if(a==1):
    print("not a prime")
else:
    if b==0:
        print('prime')
    else:
        print("not a prime")