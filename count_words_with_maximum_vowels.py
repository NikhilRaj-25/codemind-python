a=input()
l=a.split()
c=0
ans=[]
v="aeiou"
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    ans.append(c)
x=max(ans)
print(ans.count(x))