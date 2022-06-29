a=int(input())
b=a
ans1=0
ans2=1
while b:
    ans1+=b%10
    ans2=ans2*(b%10)
    b=b//10
if(ans1==ans2):
    print('Spy Number')
else:
    print('Not Spy Number')