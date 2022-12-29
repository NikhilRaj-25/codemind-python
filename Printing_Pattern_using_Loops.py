r=int(input())
for i in range(r,0,-1):
    for j in range(r,i,-1):
        print(j,end=" ")
    for j in range(1,i*2):
        print(i,end=" ")
    for j in range(i+1,r+1):
        print(j,end=" ")
    print()
for i in range(2,r+1):
    for j in range(r,i,-1):
        print(j,end=" ")
    for j in range(1,i*2):
        print(i,end=" ")
    for j in range(i+1,r+1):
        print(j,end=" ")
    print()