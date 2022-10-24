a=int(input())
if a<3:
    print('The pattern is not possible')
else:
    for i in range(0,a):
        for j in range(0,i+1):
            print("*",end="")
        print()
    for i in range(a-2,0,-1):
        for j in range(0,i+1):
            print("*",end="")
        print()
    print("*")