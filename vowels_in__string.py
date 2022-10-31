a=input()
v="aeiouAEIOU"
c=0
ans=[]
for i in a:
    if i in v and i not in ans:
        ans.append(i)
if len(ans)==0:
    print('-1')
else:
    print(*ans)