a=int(input())
l=list(map(int,input().split()))
b=0
for i in l:
    if i==0 or i==1:
        continue
    else:
        b=1
        print('False')
        break
if b==0:
    print('True')