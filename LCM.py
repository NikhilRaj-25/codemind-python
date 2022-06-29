a,b=map(int,input().split())
c=1
for i in range(1,b+1):
    c=a*i
    if c%b==0:
        print(c)
        break