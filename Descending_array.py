a=int(input())
l=list(map(int,input().split()))
b=0
for i in range(a-1):
    if l[i]<=l[i+1]:
        b=1
        print('no')
        break
if b==0:
    print('yes')