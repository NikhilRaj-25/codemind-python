def ispretty(a):
    b=a%10
    if b==2 or b==3 or b==9:
        return 1
    else:
        return 0
for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        if ispretty(j):
            c+=1
    print(c)