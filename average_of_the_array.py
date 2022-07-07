a=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
avg=float(s/a)
print('%.2f'%avg)