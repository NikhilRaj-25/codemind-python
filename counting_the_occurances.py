a=input()
b=input()
ans=0
for i in a:
    if b==i:
        ans+=1
if ans==0:
    print("-1")
else:
    print(ans)