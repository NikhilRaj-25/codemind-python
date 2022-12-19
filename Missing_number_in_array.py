for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    s1=(a*(a+1))//2
    print(s1-s)