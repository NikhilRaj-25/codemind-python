a=int(input())
x=0
n=0
for i in range(a,0,-1):
    x+=1 
    for j in range(1,i+1):
        print(x,end=' ')
        x+=1
    n+=1
    x=n
    print()