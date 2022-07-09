a=int(input())
l=list(map(int,input().split()))
p=1
for i in range(a):
    p=1
    for j in range(a):
        if j!=i:
            p=p*l[j]
    print(p,end=" ")