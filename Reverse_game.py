a=int(input())
lst=list(map(int,input().split()))
ans=[]

for i in lst:
    rem=s=0
    while i:
        rem=i%10
        s=s*10+rem
        i=i//10
    ans.append(s)
print(*ans)