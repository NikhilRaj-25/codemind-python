a=int(input())
l=list(map(int,input().split()))
b=0
for i in range(0,a-2,2):
    if (l[i]<l[i+1] and l[i+1]>l[i+2]) or (l[i]>l[i+1] and l[i+1]<l[i+2]):
        b+=1
    else:
        b=-1
        print('no')
        break
if b!=-1:
    print('yes')