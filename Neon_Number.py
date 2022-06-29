a=int(input())
sq=a*a
s=0
while sq:
    s+=sq%10
    sq=sq//10
if(s==a):
    print('Neon Number')
else:
    print('Not Neon Number')