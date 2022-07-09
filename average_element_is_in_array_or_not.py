a=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
avg=s//a
for i in l:
    if avg==i:
        print('True')
        break
else:
    print('False')