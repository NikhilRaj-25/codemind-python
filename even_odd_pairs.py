a=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
ev=od=0
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
b=len(e)
c=len(o)
for i in range(a):
    if ev>=b and od>=c:
        break
    if ev>=b:
        print(o[od],end=" ")
        od+=1
    elif od>=c:
        print(e[ev],end=" ")
        ev+=1
    else:
        print(e[ev],end=" ")
        ev+=1
        print(o[od],end=" ")
        od+=1
if a%2!=0:
    print('0')