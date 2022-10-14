for q in range(int(input())):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in a:
        if i%2==1:
            c+=1
    if c%2==1:
        c-=1
    print(c//2)