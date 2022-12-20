a=int(input())
l=list(map(int,input().split()))
c=0
arr=[]
for i in l:
    if i not in arr:
        arr.append(i)
        if i%2==1:
            c+=1
print(c)