a=input()
l=a.split()
ans=[]
for i in l:
    ans.append(i[::-1])
print(*ans)