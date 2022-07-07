a=int(input())
lst=list(map(int,input().split()))
o=e=0
for i in range(len(lst)):
    if i%2==0:
        e+=lst[i]
    else:
        o+=lst[i]
if e==o:
    print('YES')
else:
    print("NO")