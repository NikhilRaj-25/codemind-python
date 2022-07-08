a,b=map(int,input().split())
l=list(map(int,input().split()))
lst=list(map(int,input().split()))
d=set(l)
c=0
for i in d:
   if i in lst:
       c+=1
print(c)